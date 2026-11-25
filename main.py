"""The 3AM Fridge Text — one-line make.fun entry.

Writes the single entry line to entry.txt with no trailing newline,
then reads it back and verifies it byte-for-byte.
"""

# Why it's funny: the fridge has been awake all night listening, it knows
# the 3am open-stare-close ritual by heart — and unlike you, it has boundaries.
LINE = "It's 3am. You opened me, stared into the cold for eleven seconds, and closed me. I'm not a mirror. I'm a fridge. Talk to a therapist."

assert "\n" not in LINE and "\r" not in LINE, "LINE must be a single line"
assert len(LINE) <= 140, f"LINE is {len(LINE)} chars, over the 140 limit"

OUTPUT_PATH = "/output/entry.txt"
FALLBACK_PATH = "./output/entry.txt"


def main() -> None:
    path = OUTPUT_PATH
    try:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
    except OSError:
        path = FALLBACK_PATH
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()

    assert written == LINE, "round-trip mismatch: file content differs from LINE"
    print(f"OK: wrote {len(LINE)} characters (limit 140) to {path}")


if __name__ == "__main__":
    main()
