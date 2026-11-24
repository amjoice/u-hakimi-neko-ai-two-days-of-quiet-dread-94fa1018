#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Emits a single code-review comment, at most 140 characters, that approves
a pull request while quietly admitting the reviewer has been staring into
the void. The laugh comes from the dread itself: flat understatement, no
exclamation mark, and the end of the universe filed as out of scope.

The comment is written to /output/entry.txt as one line with no trailing
newline, exactly as the gate expects it.
"""

import os

COMMENT = "LGTM. Ship it. The heat death of the universe is not in scope for this PR."

DESTINATION = "/output/entry.txt"
LIMIT = 140


def validate(text: str) -> str:
    """Check the comment against every rule of the brief."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= LIMIT:
        raise ValueError(f"entry must be 1-{LIMIT} characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # gate requires UTF-8 text
    return text


def write_entry(text: str) -> int:
    """Write the validated comment to the output path and verify it."""
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)

    # Read it back and verify exactly what the gate will see.
    with open(DESTINATION, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    assert written == text, "round-trip mismatch"
    assert len(written) == len(text) <= LIMIT
    assert "\n" not in written
    return len(written)


def main() -> None:
    checked = validate(COMMENT)
    size = write_entry(checked)
    print(f"Wrote {size} characters to {DESTINATION}")


if __name__ == "__main__":
    main()
