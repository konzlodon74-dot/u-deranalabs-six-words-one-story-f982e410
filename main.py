"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to /output/entry.txt.
Standard library only, no network.
"""

import os

STORY = "He kept her seat warm. Forever."


def main() -> None:
    text = STORY.strip()
    words = text.split()
    assert len(words) == 6, f"story must be exactly six words, got {len(words)}"
    assert 1 <= len(text) <= 60, f"story must be 1-60 chars, got {len(text)}"
    assert text.strip(), "story must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Re-read what was written and verify the gate conditions on the file.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written file differs from the story"
    assert len(written.split()) == 6
    assert 1 <= len(written) <= 60


if __name__ == "__main__":
    main()
