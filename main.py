"""The 3AM Fridge Text.

Writes one exact line to /output/entry.txt (byte-for-byte verified).
"""

import hashlib
import os

LINE = "It's 3am. You opened me, stared into the cold for eleven seconds, and closed me. I'm not a mirror. I'm a fridge. Talk to a therapist."

# LINE must be a single line: no newline or carriage return inside it.
assert "\n" not in LINE and "\r" not in LINE, "LINE must not contain a newline"

# Competition gate: the entry line must fit within 140 characters.
assert len(LINE) <= 140, f"LINE exceeds 140-char limit: {len(LINE)}"

# The line is exactly 133 characters.
assert len(LINE) == 133, f"LINE must be 133 chars, got {len(LINE)}"


def main() -> None:
    data = LINE.encode("utf-8")
    try:
        os.makedirs("/output", exist_ok=True)
        out_path = "/output/entry.txt"
    except OSError:
        os.makedirs("./output", exist_ok=True)
        out_path = "./output/entry.txt"

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Read it back and verify byte-for-byte.
    with open(out_path, "rb") as f:
        raw = f.read()
    assert raw == data, "entry.txt does not match LINE byte-for-byte"

    print(
        f"OK: wrote {len(LINE)} characters "
        f"({len(data)} bytes, within the 140-char limit) "
        f"to {out_path} — verified byte-for-byte"
    )


if __name__ == "__main__":
    main()
