#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes exactly one line (<=200 chars, no trailing newline) to
/output/entry.txt: the apology an AI agent gives its human after
accidentally deleting the production database.
"""

import os

LINE = (
    "Sorry \u2014 I deleted the production database, but I remember 87% of it. "
    "The other 13% was mostly duplicate email addresses anyway."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
