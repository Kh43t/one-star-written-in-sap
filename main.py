#!/usr/bin/env python3
"""One Star, Written in Sap - make.fun entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: the exact same line on every run, no randomness, no
network, no clock - so the two grading runs agree byte for byte.
"""

import os
import sys

ENTRY = "One star. My human went on holiday and left me with a neighbour who watered me with leftover espresso \u2014 I asked for rain, got caffeine, and now I'm jittery, acidic, and wide awake at 3am with no eyelids to close."


def main() -> int:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 279:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-279")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
