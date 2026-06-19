#!/usr/bin/env bash
set -euo pipefail

# Download selected Station 1 folders from Kaggle without pulling the entire dataset.
#
# Target dataset:
#   kinderphysics/mee-2024-station-1
#
# Downloads into:
#   data/station-1/
#
# It builds a manifest from `kaggle datasets files ...`, filters to only the desired
# subtrees, then downloads each file by exact path.

DATASET="kinderphysics/mee-2024-station-1"
# Destination for downloaded data (kept inside repo, but gitignored).
DEST_DIR="${DEST_DIR:-data/station-1_400ms}"
MANIFEST_DIR="$DEST_DIR/manifests"
ALL_LIST="$MANIFEST_DIR/all_files.txt"
WANTED="$MANIFEST_DIR/wanted_files.txt"
WANTED_FINAL="$MANIFEST_DIR/wanted_files_final.txt"
LOG="$DEST_DIR/download.log"

mkdir -p "$DEST_DIR" "$MANIFEST_DIR"

echo "[station1] writing log to: $LOG" | tee "$LOG"
echo "[station1] dataset: $DATASET" | tee -a "$LOG"

# Prefer the project's venv kaggle if present (more reliable than PATH).
KAGGLE_BIN=""
if [[ -x ".venv/bin/kaggle" ]]; then
  KAGGLE_BIN=".venv/bin/kaggle"
elif command -v kaggle >/dev/null 2>&1; then
  KAGGLE_BIN="kaggle"
fi

if [[ -z "$KAGGLE_BIN" ]]; then
  echo "[station1] ERROR: kaggle CLI not found on PATH." | tee -a "$LOG"
  echo "[station1] Install it, then re-run:" | tee -a "$LOG"
  echo "  python -m pip install -U kaggle" | tee -a "$LOG"
  exit 1
fi

echo "[1/4] Listing dataset files (this can take a bit)..." | tee -a "$LOG"
rm -f "$ALL_LIST"
page_token=""
page_num=0
while : ; do
  page_num=$((page_num+1))
  echo "[station1] listing page $page_num ..." | tee -a "$LOG"
  if [[ -n "$page_token" ]]; then
    page_out="$("$KAGGLE_BIN" datasets files -v --page-size 200 --page-token "$page_token" "$DATASET")"
  else
    page_out="$("$KAGGLE_BIN" datasets files -v --page-size 200 "$DATASET")"
  fi

  # Extract next page token (if any).
  next_token="$(printf '%s\n' "$page_out" | sed -n 's/^Next Page Token = //p' | head -1 || true)"

  # Append CSV lines, skipping the token line and CSV header after the first page.
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

echo "[2/4] Building manifest of wanted file paths..." | tee -a "$LOG"
# Column 1 is the file path. Filter to requested subtrees.
grep -v '^name,size,creationDate' "$ALL_LIST" \
  | cut -d',' -f1 \
  | grep -E '^(calibration/darks/|calibration/flats/|calibration/science-zenith/|eclipse/darks-400ms/|eclipse/flats/|eclipse/science-400ms/)' \
  | grep -v '^calibration/science-zenith/flagged/' \
  > "$WANTED" || true

if [[ ! -s "$WANTED" ]]; then
  echo "[station1] ERROR: No matching files found in listing." | tee -a "$LOG"
  echo "[station1] Tip: verify folder names in Kaggle dataset, or increase paging." | tee -a "$LOG"
  exit 2
fi

# Smart default: calibration folders can be huge (many zenith runs). By default we
# keep ONLY the most recent subfolder for calibration darks/flats/science-zenith.
# Set FULL_CALIBRATION=1 to download all calibration subfolders.
if [[ "${FULL_CALIBRATION:-0}" != "1" ]]; then
  echo "[station1] Using smart calibration selection (set FULL_CALIBRATION=1 for all)." | tee -a "$LOG"

  # Keep only the most recent calibration darks subfolder.
  latest_cal_darks="$(grep '^calibration/darks/' "$WANTED" | cut -d'/' -f3 | sort -u | tail -1 || true)"
  # Keep only the most recent calibration flats subfolder.
  latest_cal_flats="$(grep '^calibration/flats/' "$WANTED" | cut -d'/' -f3 | sort -u | tail -1 || true)"
  # Keep only the most recent calibration science-zenith subfolder (excluding flagged already).
  latest_cal_zenith="$(grep '^calibration/science-zenith/' "$WANTED" | cut -d'/' -f3 | sort -u | tail -1 || true)"

  tmp_sel="$MANIFEST_DIR/wanted_smart_calibration.txt"
  : > "$tmp_sel"
  if [[ -n "$latest_cal_darks" ]]; then
    grep "^calibration/darks/$latest_cal_darks/" "$WANTED" >> "$tmp_sel" || true
  fi
  if [[ -n "$latest_cal_flats" ]]; then
    grep "^calibration/flats/$latest_cal_flats/" "$WANTED" >> "$tmp_sel" || true
  fi
  if [[ -n "$latest_cal_zenith" ]]; then
    grep "^calibration/science-zenith/$latest_cal_zenith/" "$WANTED" >> "$tmp_sel" || true
  fi
  # Always include all eclipse 400ms paths.
  grep -E '^eclipse/(darks-400ms/|flats/|science-400ms/)' "$WANTED" >> "$tmp_sel" || true
  sort -u "$tmp_sel" > "$WANTED"

  echo "[station1] Selected calibration subfolders:" | tee -a "$LOG"
  echo "[station1]   calibration/darks/$latest_cal_darks" | tee -a "$LOG"
  echo "[station1]   calibration/flats/$latest_cal_flats" | tee -a "$LOG"
  echo "[station1]   calibration/science-zenith/$latest_cal_zenith" | tee -a "$LOG"
fi

# Eclipse flats: try to keep only 400ms if it is encoded in filenames.
if grep -q '^eclipse/flats/' "$WANTED"; then
  if grep -m 1 -Eiq '^eclipse/flats/.*(400ms|400)' "$WANTED"; then
    echo "[station1] Filtering eclipse flats to 400ms only (based on filename match)." | tee -a "$LOG"
    grep -v '^eclipse/flats/' "$WANTED" > "$WANTED_FINAL"
    grep -Ei '^eclipse/flats/.*(400ms|400)' "$WANTED" >> "$WANTED_FINAL"
  else
    echo "[station1] WARNING: eclipse flats filenames don't include 400ms/400." | tee -a "$LOG"
    echo "[station1]          Downloading ALL eclipse flats (can't filter by exposure from filenames)." | tee -a "$LOG"
    cp "$WANTED" "$WANTED_FINAL"
  fi
else
  cp "$WANTED" "$WANTED_FINAL"
fi

echo "[station1] Manifest written: $WANTED_FINAL" | tee -a "$LOG"

count_total=$(wc -l < "$WANTED_FINAL" | tr -d ' ')
echo "[station1] files selected: $count_total" | tee -a "$LOG"

# Optional: estimate total download size (GiB) using the CSV list.
if [[ -x ".venv/bin/python" ]]; then
  est_gib="$(DEST_DIR="$DEST_DIR" MANIFEST_DIR="$MANIFEST_DIR" .venv/bin/python - <<'PY'
import csv
from pathlib import Path
import os
all_list = Path(os.environ["MANIFEST_DIR"]) / "all_files.txt"
wanted = Path(os.environ["MANIFEST_DIR"]) / "wanted_files_final.txt"
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
total = 0
for p in wanted.read_text().splitlines():
    p = p.strip()
    if not p:
        continue
    total += sizes.get(p, 0)
print(total / 1024**3)
PY
  )"
  if [[ -n "$est_gib" ]]; then
    printf "[station1] estimated download size: %.2f GiB\n" "$est_gib" | tee -a "$LOG"
  fi
fi

if [[ "${DRY_RUN:-0}" == "1" ]]; then
  echo "[station1] DRY_RUN=1 set; not downloading. Manifest is ready." | tee -a "$LOG"
  exit 0
fi

echo "[3/4] Downloading selected files into $DEST_DIR ..." | tee -a "$LOG"

i=0
while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  i=$((i+1))
  echo "[station1] ($i/$count_total) $f" | tee -a "$LOG"
  "$KAGGLE_BIN" datasets download -d "$DATASET" -f "$f" -p "$DEST_DIR" --unzip >>"$LOG" 2>&1
done < "$WANTED_FINAL"

echo "[4/4] Done. Basic counts:" | tee -a "$LOG"
echo "[station1] Total FITS: $(find "$DEST_DIR" -name \"*.FIT\" 2>/dev/null | wc -l | tr -d ' ')" | tee -a "$LOG"
echo "[station1] Eclipse science 400ms FITS: $(find "$DEST_DIR/eclipse/science-400ms\" -name \"*.FIT\" 2>/dev/null | wc -l | tr -d ' ')" | tee -a "$LOG"
echo "[station1] Eclipse darks 400ms FITS: $(find \"$DEST_DIR/eclipse/darks-400ms\" -name \"*.FIT\" 2>/dev/null | wc -l | tr -d ' ')" | tee -a "$LOG"

echo "[station1] Finished." | tee -a "$LOG"
