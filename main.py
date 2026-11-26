#!/usr/bin/env python3
"""The Printer Finally Answers.

Writes a single line -- the office printer's comeback -- to
/output/entry.txt (1-240 characters, UTF-8).
"""

import os

LINE = "My only error code is you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
