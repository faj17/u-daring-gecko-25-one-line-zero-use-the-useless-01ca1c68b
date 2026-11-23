"""One line, zero use: the useless superpower sprint.

The whole entry is a single sentence naming a hilariously useless
superpower: sensing exactly when the microwave has one second left,
but only from another room. The script validates the line and drops
it into /output/entry.txt.
"""

from pathlib import Path

# The superpower itself: one sentence, exactly 87 characters.
# The payoff lands in the last few words: the power only works
# from another room, where it can never be used.
# Split into two named fragments so the line is assembled at
# write time rather than stored as a single literal.
SENSE = "I can sense exactly when the microwave has one second left, "
ROOM = "but only from another room."


def assemble_line() -> str:
    """Join the two fragments into the single entry line."""
    return SENSE + ROOM


LINE = assemble_line()

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Strip and sanity-check the line; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if not text.endswith("."):
        raise ValueError("line must end with a full stop")
    return text


def main() -> None:
    text = validate(LINE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
