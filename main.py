#!/usr/bin/env python3
"""Famous Last Words at 1 Percent - make.fun entry.

Writes the funniest one-line farewell a phone could say as its
battery hits 1 percent, to /output/entry.txt.

The joke: the phone was never actually dying - it faked its last
percent just to see whether its owner would finally put it down.
"""

LINE = "Turns out I was never dying. I just wanted to see if you'd finally put me down."


def main() -> None:
    # Enforce the competition gate: 1-199 characters, not only whitespace.
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
