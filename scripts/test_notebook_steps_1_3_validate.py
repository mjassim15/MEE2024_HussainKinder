#!/usr/bin/env python3
"""Execute notebook cells for Setup + Steps 1 & 3 validate (no do_stack)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
NB_PATH = REPO / "MEE2024_Notebook_Version.ipynb"


def strip_ipython_magics(code: str) -> str:
    return "\n".join(line for line in code.splitlines() if not line.lstrip().startswith("%"))


def exec_cell(code: str, globs: dict, label: str) -> None:
    print(f"\n--- {label} ---")
    code = strip_ipython_magics(code)
    try:
        exec(compile(code, f"<{label}>", "exec"), globs)
    except Exception as exc:
        print(f"FAIL: {exc}")
        raise
    print(f"OK: {label}")


def main() -> int:
    nb = json.loads(NB_PATH.read_text())
    cells = {i: "".join(c["source"]) for i, c in enumerate(nb["cells"])}

    globs: dict = {"__name__": "__main__"}

    # Skip database init in setup for speed — mock if prepare_triangles exists
    setup = cells[2]
    setup = setup.replace(
        'print("Initializing star catalog database...")\n'
        "database_cache.prepare_triangles()\n"
        'print("✅ Database ready!")',
        'print("(test) skipping database_cache.prepare_triangles()")',
    )

    exec_cell(setup, globs, "Setup")

    # Step 1: config then validate
    exec_cell(cells[4], globs, "Step 1 config")
    exec_cell(cells[6], globs, "Step 1 validate")
    assert len(globs["valid_zenith_light_files"]) == 10

    # Step 3: config then validate (fresh globs without zenith valid lists is ok)
    # Resolve cells by content (indices shift if markdown inserted)
    step3_cfg = next(i for i, c in enumerate(nb["cells"]) if "STEP 3 (GUI TAB 1)" in cells[i])
    step3_val = next(
        i for i, c in enumerate(nb["cells"]) if "VALIDATE ECLIPSE INPUT FILES" in cells[i]
    )
    exec_cell(cells[step3_cfg], globs, "Step 3 config")
    exec_cell(cells[step3_val], globs, "Step 3 validate")
    assert len(globs["valid_eclipse_light_files"]) == 10
    assert len(globs["valid_eclipse_dark_files"]) == 10
    assert globs["step3_options"]["blob_radius_extra"] == 200

    # Negative test: validate without config raises NameError (Python's natural
    # error — clear enough; explicit guard removed in favor of self-containment).
    globs2: dict = {"__name__": "__main__"}
    try:
        exec(compile(cells[6], "<step1 validate no config>", "exec"), globs2)
        print("FAIL: expected NameError for missing zenith_light_files")
        return 1
    except NameError as e:
        assert "zenith_light_files" in str(e), e
        print(f"OK: Step 1 validate without config -> NameError as expected")

    # Step 3 validate without Setup (bootstrap path)
    globs3: dict = {"__name__": "__main__"}
    exec_cell(cells[step3_cfg], globs3, "Step 3 config (no setup)")
    exec_cell(cells[step3_val], globs3, "Step 3 validate (no setup)")
    assert len(globs3["valid_eclipse_light_files"]) == 10

    print("\n=== ALL VALIDATE TESTS PASSED ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
