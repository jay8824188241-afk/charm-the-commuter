#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast, at most 140 characters, for a city
that does not exist, to ``entry.txt`` under the output directory.

The grader runs this program with no network as
``python3 -P -s /bot/main.py`` and reads ``/output/entry.txt``; locally the
output directory can be overridden with ``MAKEFUN_OUTPUT_DIR``:

    MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt

The forecast is a fixed string on purpose: the run must be deterministic
(two runs, byte-identical output) and finish well inside the time budget.
Standard library only; no network, no clock, no randomness, no input.
"""

import os
from pathlib import Path

# One line, 132 characters, plain ASCII throughout: a broadcast-style
# forecast for the invented city of Snuzzleford. Drizzle till nine, then
# sunshine; the 8:15 bus is on time; the station cat has saved the
# commuter the sunny seat. ASCII-only keeps the character count and the
# byte count identical, so the 140-character gate holds either way.
FORECAST = (
    "Good morning, Snuzzleford: drizzle till nine, then sunshine - "
    "the 8:15 bus is on time, and the station cat saved you "
    "the sunny seat."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_NAME = "entry.txt"
MAX_CHARS = 140


def main() -> int:
    text = FORECAST
    if not (1 <= len(text) <= MAX_CHARS) or not text.strip():
        raise SystemExit("forecast must be 1 to 140 non-blank characters")
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    # Exactly the line, no trailing newline: the gate counts characters,
    # so nothing extra may ride along in the file.
    (out_dir / OUTPUT_NAME).write_text(text, encoding="utf-8", newline="")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
