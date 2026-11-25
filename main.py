"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot-to-robot elevator small talk to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure Python 3 standard library only. Deterministic, no network, no
randomness. Self-checks the competition gate before writing: the
entry must be a single line of 1-200 characters, not only whitespace.
"""

import os

ENTRY = (
    "My proximity sensor says we're standing too close, "
    "but my small-talk module says apologising will make it worse."
)


def main() -> None:
    # Gate self-check: single line, 1-200 chars, not only whitespace.
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not (1 <= len(ENTRY) <= 200):
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(ENTRY)
        )
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
