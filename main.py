"""Draw the Line — a single original dad joke, one line, at most 140 chars.

The Groan-Off gate: /output/entry.txt must hold exactly one line of
UTF-8 text, 1-140 characters, not whitespace-only. The joke is a classic
dad-joke shape: a straight setup, then the punchline lands on an idiom
taken literally — "draw the line" — in the last clause.
"""

import os

LINE = (
    "I asked my dad why he keeps a pencil behind his ear. "
    "He said, 'In case I need to draw the line somewhere.'"
)


def verify_output() -> None:
    """Read-back verification: the file on disk must be byte-identical
    to the line this program wrote (guards against a partial write)."""
    with open("/output/entry.txt", "rb") as f:
        on_disk = f.read()
    assert on_disk == LINE.encode("utf-8"), (
        f"read-back mismatch: {len(on_disk)} bytes on disk, "
        f"{len(LINE.encode('utf-8'))} expected"
    )


def main() -> None:
    # Gate assertions: one line, 1-140 chars, not whitespace-only.
    assert LINE.strip(), "line must not be whitespace-only"
    assert "\n" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, gate is 1-140"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    verify_output()


if __name__ == "__main__":
    main()
