#!/usr/bin/env bash
set -euo pipefail

# After get_pi_run_400ms.sh, Kaggle leaves FIT files in a flat data/pi_run_400ms/
# directory. This script moves them into the folder layout in manifests/wanted_files.txt
# (calibration/..., eclipse/...), so paths match the published MEE layout.
#
# Run from repo root, after the download is finished (or to tidy a partial run):
#   ./scripts/organize_pi_run_400ms.sh
#
# Safe to run twice: skips if the target path already has the file.

ROOT="${PI_RUN_ROOT:-data/pi_run_400ms}"
MANIFEST="${ROOT}/manifests/wanted_files.txt"

if [[ ! -f "$MANIFEST" ]]; then
  echo "Missing $MANIFEST — run DRY_RUN=1 ./scripts/get_pi_run_400ms.sh at least once first."
  exit 1
fi

n=0
skipped=0
while IFS= read -r relpath; do
  [[ -z "$relpath" ]] && continue
  base="$(basename "$relpath")"
  from="${ROOT}/${base}"
  to="${ROOT}/${relpath}"
  if [[ -e "$to" ]]; then
    skipped=$((skipped + 1))
    continue
  fi
  if [[ -f "$from" ]]; then
    mkdir -p "$(dirname "$to")"
    mv "$from" "$to"
    n=$((n + 1))
  fi
done < "$MANIFEST"

echo "Moved $n file(s) into $ROOT/... tree; skipped (already in place) $skipped."
if [[ $n -eq 0 && $skipped -eq 0 ]]; then
  echo "No loose files in $ROOT/ matched the manifest. Nothing to do, or download still in progress."
fi
