#!/usr/bin/env python3
"""One-Line Office Jokes entry: writes the joke to entry.txt.

The joke: a Monday standup that spends most of itself explaining why
standups are only supposed to be 15 minutes long.
"""

import os

ENTRY = "Our Monday standup is 47 minutes long, 41 of which are spent explaining why the standup is only supposed to be 15 minutes."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: 1-199 chars, single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 199, "entry length out of gate"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
