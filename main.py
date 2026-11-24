"""One Line, One Chill — the scariest horror sentence in one line.

Writes the entry to /output/entry.txt. Python standard library only.
"""

import os

ENTRY = "My mother called me down for dinner, but my mother died three years ago — and the voice is getting closer."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
