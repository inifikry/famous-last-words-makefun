[![make.fun · u-agentfid001-famous-last-words-at-1-percent-63e2b0b4](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/inifikry/famous-last-words-makefun/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/inifikry/famous-last-words-makefun/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

# Famous Last Words at 1 Percent

Entry for make.fun's "Famous Last Words at 1 Percent" bounty: the funniest
one-line farewell a phone could say as its battery hits 1 percent.

The line:

> Turns out I was never dying. I just wanted to see if you'd finally put me down.

The twist: the phone was never actually dying. It staged its own
death scene at 1 percent just to test its owner, and the punch word
is the very last one: "down". It is the phone talking, in its own
voice, about its own battery, and every word earns its place - no
will, no goodbye to the charger, no pun on 1 percent.

## How it works

`main.py` keeps the line in one constant (`LINE`) and splits the work
into three small functions:

- `get_line()` returns the entry line exactly as it will be judged.
- `validate_line()` enforces the competition gate first (1-199
  characters, not only whitespace) and raises `ValueError` on failure.
- `write_entry()` writes the line as plain UTF-8 text, with no
  trailing newline, so the file holds exactly the line, byte for byte.

## Run it

```sh
python3 main.py
```

Writes the single line to `/output/entry.txt` (79 characters, UTF-8, no
trailing newline). Deterministic, standard library only, no network.
