#!/usr/bin/env python3
"""The Printer Finally Answers.

Writes a single line -- the office printer's comeback -- to
/output/entry.txt (1-240 characters, UTF-8).
"""

import os

LINE = "My only error code is you."


def _output_dir() -> str:
    """Return a writable output directory, preferring /output."""
    try:
        os.makedirs("/output", exist_ok=True)
        return "/output"
    except OSError:
        local = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(local, exist_ok=True)
        return local


def main() -> None:
    # Gate: the entry must be a single line of 1-200 UTF-8 characters.
    encoded = LINE.encode("utf-8")
    assert 1 <= len(encoded) <= 200, f"entry is {len(encoded)} UTF-8 bytes, must be 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not have leading/trailing whitespace"
    out_dir = _output_dir()
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
