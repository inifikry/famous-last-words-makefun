#!/usr/bin/env python3
"""Famous Last Words at 1 Percent - make.fun entry.

Writes the funniest one-line farewell a phone could say as its
battery hits 1 percent, to /output/entry.txt.

Why the line is funny: it flips the whole premise. The phone is not
dying at all - it staged its own death scene at 1 percent just to
test its owner. The twist lands in the second sentence ("I just
wanted to see..."), and the punch word is the very last one: "down".
It is the phone talking, in its own voice, about its own battery,
and every word earns its place - no will, no goodbye to the charger,
no pun on 1 percent.
"""

# Competition gate (see RULES.txt): 1-199 characters, not only whitespace.
MIN_LENGTH = 1
MAX_LENGTH = 199
OUTPUT_PATH = "/output/entry.txt"

LINE = "Turns out I was never dying. I just wanted to see if you'd finally put me down."


def get_line() -> str:
    """Return the entry line, exactly as it will be judged."""
    return LINE


def validate_line(line: str) -> None:
    """Enforce the competition gate before anything is written.

    The gate is a sealed scorer, so the program checks the same rules
    itself first: 1-199 characters and not only whitespace.
    """
    if not MIN_LENGTH <= len(line) <= MAX_LENGTH:
        raise ValueError(
            f"line is {len(line)} chars, must be {MIN_LENGTH}-{MAX_LENGTH}"
        )
    if not line.strip():
        raise ValueError("line must not be only whitespace")


def write_entry(line: str, path: str = OUTPUT_PATH) -> None:
    """Write the line to the output file as plain UTF-8 text.

    No trailing newline: the file holds exactly the line, byte for
    byte, so the judge reads what was written here and nothing else.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


def main() -> None:
    line = get_line()
    validate_line(line)
    write_entry(line)


if __name__ == "__main__":
    main()
