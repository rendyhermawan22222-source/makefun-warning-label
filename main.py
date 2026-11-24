#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the single funniest safety warning label that should come printed
on every human being to /output/entry.txt: exactly one line, plain ASCII,
at most 160 characters. Then reads it back and verifies it, exiting
non-zero on any mismatch.

The label (133 chars):

    WARNING: The check-engine light has been on since 2014. The driver
    named it, stopped seeing it, and now calls it a personality trait.

Why this line: it reads like a real dashboard warning applied to a
human (the human is the car, the driver is the human), escalates in
three beats -- named it, stopped seeing it, calls it a personality
trait -- and the last six words reframe the hazard as identity. The
ignored check-engine light is a universally recognised human quirk,
and no entry in the field uses this angle.
"""

import sys
from pathlib import Path

LABEL = (
    "WARNING: The check-engine light has been on since 2014. "
    "The driver named it, stopped seeing it, and now calls it "
    "a personality trait."
)

MAX_CHARS = 160
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> int:
    if len(LABEL) > MAX_CHARS:
        print(
            f"error: label is {len(LABEL)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    if not LABEL.isascii():
        print("error: label is not ASCII", file=sys.stderr)
        return 1
    if "\n" in LABEL or "\r" in LABEL:
        print("error: label is not a single line", file=sys.stderr)
        return 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LABEL + "\n", encoding="ascii")

    # Read-back verification: exactly the line, one line, ASCII, <=160 chars.
    read_back = OUTPUT_PATH.read_text(encoding="ascii")
    lines = read_back.splitlines()
    if len(lines) != 1 or lines[0] != LABEL:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    if len(lines[0]) > MAX_CHARS:
        print("error: read-back line over the limit", file=sys.stderr)
        return 1
    if not read_back.endswith("\n") or read_back.count("\n") != 1:
        print("error: file must hold exactly one line plus its newline",
              file=sys.stderr)
        return 1

    print(f"wrote {OUTPUT_PATH} ({len(LABEL)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
