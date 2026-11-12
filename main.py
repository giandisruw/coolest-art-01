#!/usr/bin/env python3
"""The Gardener of Thunderclouds - make.fun coolest-art-01 entry (v2).

Copies the bundled artwork (entry.png, a tiny gardener in a yellow
raincoat watering a storm cloud from a ladder, so lightning blooms
into flowers) to the output directory make.fun grades:
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).

Standard library only, deterministic, no network access.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_NAME = "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing artwork: {SOURCE}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    shutil.copyfile(SOURCE, target)
    # Fail loudly rather than hand the grader a truncated copy.
    if target.stat().st_size != SOURCE.stat().st_size:
        print("copy size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
