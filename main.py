"""Roast Your Own Agent entry.

Writes a single one-line roast of our own agent to entry.txt.
Standard library only. No trailing newline in the output file.
"""

import os

ENTRY = (
    "My agent agreed with me, then agreed with the opposite, "
    "then asked which I preferred."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
