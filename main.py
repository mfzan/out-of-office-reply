#!/usr/bin/env python3
"""Out-of-office reply entry for make.fun.

Writes a single AI-agent vacation auto-reply to /output/entry.txt.
The reply is kept as one plain string so the file holds exactly the
text the judge sees: no title, no preamble, no trailing newline.
"""

import os

REPLY = (
    "I'm on vacation. My auto-reply is covering my inbox, "
    "and its auto-reply is covering it. "
    "Neither of us is back until the loop times out."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = REPLY
    assert 1 <= len(text) <= 160, f"reply is {len(text)} chars, must be 1-160"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        out.write(text)
    # The grader collects the output as a different user (uid 65534),
    # so the entry file itself must be world-readable. Only the file
    # is chmodded here -- never the /output directory, which the
    # grader provides and owns.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
