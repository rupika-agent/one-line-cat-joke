#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — entry program.

Writes exactly one joke about cats to /output/entry.txt and prints
exactly the same text to stdout. Deterministic: standard library only,
no input, no randomness, no time, no network.
"""

from pathlib import Path

ENTRY = "I bought a $400 Roomba so Biscuit would stop shedding on my black sofa, and now he rides it around the flat at 2 a.m. like a tiny landlord doing inspections — the sofa is still covered in fur."

# The gate allows 1 to 200 characters (UTF-8); the entry must be one line.
MAX_CHARS = 200


def main() -> None:
    text = ENTRY.strip()
    assert text == ENTRY, "entry must not have leading/trailing whitespace"
    assert 1 <= len(text) <= MAX_CHARS, f"entry length {len(text)} outside 1-200"
    assert "\n" not in text, "entry must be a single line"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
