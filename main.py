#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one code-review comment, a single line of at most 140 characters
that approves a pull request while carrying quiet existential dread,
to /output/entry.txt.

The comment was written for the judge's brief: approval first, the laugh
coming from the dread itself, flat understatement, no exclamation, and a
fresh turn — the end of the universe filed as out of scope.
"""

import os

ENTRY = "LGTM. Ship it. The heat death of the universe is not in scope for this PR."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # gate requires UTF-8 text

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Read it back and verify exactly what the gate will see.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "round-trip mismatch"
    assert len(written) == len(text) <= MAX_CHARS
    assert "\n" not in written
    print(f"Wrote {len(written)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
