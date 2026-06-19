#!/usr/bin/env bash
# Launch MEE2024 GUI using the project virtual environment.
# Uses SYSTEM_VERSION_COMPAT=0 to avoid macOS version mis-detection with some wheels.

set -euo pipefail
cd "$(dirname "$0")"

export SYSTEM_VERSION_COMPAT="${SYSTEM_VERSION_COMPAT:-0}"

if [[ ! -d .venv ]]; then
  echo "Missing .venv. Create it first, e.g.:"
  echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
  echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
  echo "  uv venv --python 3.12 .venv"
  echo "  uv pip install -r requirements.txt --python .venv/bin/python"
  exit 1
fi

# shellcheck source=/dev/null
source .venv/bin/activate
exec python -m mee2024.main
