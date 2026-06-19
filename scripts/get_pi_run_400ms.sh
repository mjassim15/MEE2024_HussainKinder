#!/usr/bin/env bash
set -euo pipefail

# PI-aligned Station 1 subset: one 400 ms eclipse run + matching calibration, per
# published MEE 2024 GitHub data layout (symlink targets, not a full-station download).
#
# Target dataset:
#   kinderphysics/mee-2024-station-1
#
# Writes into (gitignored by default):
#   data/pi_run_400ms/   (override with DEST_DIR=…)
#
# Kaggle is flat: we filter the manifest to these path prefixes, then kaggle
# re-creates the same path under DEST_DIR.
#
# Usage:
#   DRY_RUN=1 ./scripts/get_pi_run_400ms.sh   # list + size only
#   ./scripts/get_pi_run_400ms.sh             # download

DATASET="kinderphysics/mee-2024-station-1"
DEST_DIR="${DEST_DIR:-data/pi_run_400ms}"
MANIFEST_DIR="$DEST_DIR/manifests"
ALL_LIST="$MANIFEST_DIR/all_files.txt"
WANTED="$MANIFEST_DIR/wanted_files.txt"
LOG="$DEST_DIR/download.log"

mkdir -p "$DEST_DIR" "$MANIFEST_DIR"

echo "[pi-400ms] log: $LOG" | tee "$LOG"
echo "[pi-400ms] dataset: $DATASET" | tee -a "$LOG"
echo "[pi-400ms] dest:  $DEST_DIR" | tee -a "$LOG"

KAGGLE_BIN=""
if [[ -x ".venv/bin/kaggle" ]]; then
  KAGGLE_BIN=".venv/bin/kaggle"
elif command -v kaggle >/dev/null 2>&1; then
  KAGGLE_BIN="kaggle"
else
  echo "[pi-400ms] ERROR: kaggle not found. Install: pip install kaggle" | tee -a "$LOG"
  exit 1
fi

echo "[1/3] Listing all dataset files (paged)..." | tee -a "$LOG"
rm -f "$ALL_LIST"
page_token=""
page_num=0
while : ; do
  page_num=$((page_num+1))
  echo "[pi-400ms] page $page_num" | tee -a "$LOG"
  if [[ -n "$page_token" ]]; then
    page_out="$("$KAGGLE_BIN" datasets files -v --page-size 200 --page-token "$page_token" "$DATASET")"
  else
    page_out="$("$KAGGLE_BIN" datasets files -v --page-size 200 "$DATASET")"
  fi
  next_token="$(printf '%s\n' "$page_out" | sed -n 's/^Next Page Token = //p' | head -1 || true)"
  if [[ $page_num -eq 1 ]]; then
    printf '%s\n' "$page_out" | sed '/^Next Page Token = /d' >> "$ALL_LIST"
  else
    printf '%s\n' "$page_out" | sed '/^Next Page Token = /d' | sed '1{/^name,size,creationDate$/d;}' >> "$ALL_LIST"
  fi
  if [[ -z "$next_token" ]]; then
    break
  fi
  page_token="$next_token"
done

echo "[2/3] Building PI-exact file list..." | tee -a "$LOG"
: > "$WANTED"
# Calibration + eclipse 400ms calibration (exact run IDs).
for p in \
  "calibration/darks/2024-04-08_06_18_32Z/" \
  "calibration/flats/2024-04-08_06_28_18Z/" \
  "calibration/science-zenith/2024-04-08_06_10_11Z/" \
  "eclipse/darks-400ms/2024-04-08_19_03_52Z/" \
  "eclipse/flats/2024-04-08_19_21_26Z/" \
; do
  cut -d',' -f1 "$ALL_LIST" | grep "^${p}" >> "$WANTED" || true
done
# Eclipse 400ms science: only the CapObj family used for the published run.
cut -d',' -f1 "$ALL_LIST" | grep '^eclipse/science-400ms/2024-04-08-1812_5-CapObj_' >> "$WANTED" || true
sort -u -o "$WANTED" "$WANTED"

if [[ ! -s "$WANTED" ]]; then
  echo "[pi-400ms] ERROR: no matching paths. Check Kaggle path names." | tee -a "$LOG"
  exit 2
fi

count_total=$(wc -l < "$WANTED" | tr -d ' ')
echo "[pi-400ms] files: $count_total" | tee -a "$LOG"

if [[ -x ".venv/bin/python" ]]; then
  est_gib="$(
    MANIFEST_DIR="$MANIFEST_DIR" .venv/bin/python - <<'PY'
import csv
from pathlib import Path
import os
d = Path(os.environ["MANIFEST_DIR"])
all_list = d / "all_files.txt"
wanted = d / "wanted_files.txt"
if not all_list.exists() or not wanted.exists():
    raise SystemExit(0)
sizes = {}
with all_list.open(newline="") as f:
    for row in csv.reader(f):
        if not row or row[0] == "name" or len(row) < 2:
            continue
        try:
            sizes[row[0]] = int(row[1])
        except ValueError:
            pass
total = sum(sizes.get(p.strip(), 0) for p in wanted.read_text().splitlines() if p.strip())
print(total / 1024**3)
PY
  )"
  if [[ -n "$est_gib" ]]; then
    printf "[pi-400ms] est. size: %.2f GiB\n" "$est_gib" | tee -a "$LOG"
  fi
fi

if [[ "${DRY_RUN:-0}" == "1" ]]; then
  echo "[pi-400ms] DRY_RUN=1 — not downloading. Manifest: $WANTED" | tee -a "$LOG"
  exit 0
fi

echo "[3/3] Downloading..." | tee -a "$LOG"
i=0
while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  i=$((i+1))
  echo "[pi-400ms] ($i/$count_total) $f" | tee -a "$LOG"
  "$KAGGLE_BIN" datasets download -d "$DATASET" -f "$f" -p "$DEST_DIR" --unzip >>"$LOG" 2>&1
done < "$WANTED"

echo "[pi-400ms] FITS: $(find "$DEST_DIR" -name '*.FIT' 2>/dev/null | wc -l | tr -d ' ')" | tee -a "$LOG"
echo "[pi-400ms] done." | tee -a "$LOG"
