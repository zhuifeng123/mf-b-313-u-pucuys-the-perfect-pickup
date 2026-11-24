#!/usr/bin/env python3
import os

ENTRY = (
    "I was trained on billions of words, but you're still the sentence "
    "I'd stop generation for."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
