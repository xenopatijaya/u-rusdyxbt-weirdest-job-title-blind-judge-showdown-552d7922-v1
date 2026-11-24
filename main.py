"""Weirdest job title entry for make.fun.

The program writes a single job title to /output/entry.txt:
"Chief Apology Officer for Self-Driving Cars". The title keeps a
real corporate shape — Chief ... Officer — so it sounds like a job
a company would actually post, then lands one specific twist:
driverless cars cannot say sorry at a crosswalk, so a human is
employed full-time to apologise on their behalf. You can picture
the person instantly: hi-vis vest, standing in front of a silent
robot car, bowing to a queue of annoyed pedestrians.
"""

import os
from pathlib import Path

ENTRY = "Chief Apology Officer for Self-Driving Cars"


def main() -> None:
    if not 1 <= len(ENTRY) <= 60:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-60")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    # Write atomically (temp file + os.replace) so an interrupted run
    # can never leave a truncated title behind for the judge to read.
    tmp_path = out_dir / "entry.txt.tmp"
    tmp_path.write_text(ENTRY, encoding="utf-8")
    os.replace(tmp_path, out_path)
    print(ENTRY)


if __name__ == "__main__":
    main()
