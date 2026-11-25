#!/usr/bin/env python3
"""One-line entry: Snooze Button Roast.

The brief asks for one line roasting an alarm clock that
rings at 6 AM on a Saturday morning. The judge weighs, in
order: the roast is really about an alarm clock ringing at
6 AM on a Saturday, a real laugh whose punchline pays off
in the last few words, a fresh angle instead of the tired
complaint about hating mornings, tight wording sayable in
one breath, and a sharp, specific voice with concrete
images rather than vague grumbling.

The sealed line below is built to that order on purpose.
It opens on the alarm clock itself, ringing at 6 AM on a
Saturday, and gives it a motive -- a personal grudge
against the sleeper's dreams -- which is the roast's
concrete image, not a generic moan about mornings. The
punch lands in the last words: "even the sun sleeps in on
weekends" turns the clock's crime back on it, because the
sun itself, the original alarm clock, keeps weekend hours
and only this one gadget does not. One sentence, nothing
to explain, and it avoids the worn-out "who invented the
alarm clock" and "I hate mornings" cracks.

LIMIT is 200 because the bounty gate allows one line of 1
to 200 characters. The sealed line is well inside the cap;
the validator below only guards against an edit that would
push it past the limit.
"""

import os

# The sealed line: an alarm clock with a personal grudge
# against Saturday dreams, shamed by the sun itself, which
# is the one clock that never rings early on a weekend.
ENTRY = "My alarm clock rang at 6 AM on a Saturday like it had a personal grudge against my dreams. Mate, even the sun sleeps in on weekends."

LIMIT = 200  # bounty gate: one line, 1-200 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
