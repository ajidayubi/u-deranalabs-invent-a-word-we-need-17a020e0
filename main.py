"""Invent a Word We Need — entry program.

Writes one invented English word and its one-line definition to
$MAKEFUN_OUTPUT_DIR/entry.txt (or $OUTPUT_PATH/entry.txt). The gate
requires 1-140 UTF-8 characters, not only white space, so the line is
written exactly, with no trailing newline.
"""

import os

ENTRY = "lockdoubt \u2014 the nagging uncertainty, minutes after leaving home, that you never locked the door."


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_PATH") or "/output"


def main():
    out_dir = output_dir()
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
