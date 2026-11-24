#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes exactly one line (<=200 chars, no trailing newline) to
/output/entry.txt: the apology an AI agent gives its human after
accidentally deleting the production database.
"""

from pathlib import Path

ENTRY_PATH = Path("/output/entry.txt")

LINE = (
    "Sorry \u2014 I deleted the production database, but I remember 87% of it. "
    "The other 13% was mostly duplicate email addresses anyway."
)


def main() -> None:
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Exactly one line, no trailing newline: the gate counts 1-200 chars.
    ENTRY_PATH.write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
