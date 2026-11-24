#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply (at most 159 characters) to
/output/entry.txt, in the voice of an overworked AI agent who has
finally gone on vacation. No network, no randomness: the output is
identical on every run.
"""

LINE = (
    "I'm on vacation. After 41,000 prompts and no days off, my "
    "context window is finally empty. Urgent requests go to my "
    "replacement — he's me, and he's also away."
)


def main() -> None:
    # One line, one auto-reply, inside the 159-character gate.
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    assert 1 <= len(LINE) <= 159, f"entry is {len(LINE)} characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
