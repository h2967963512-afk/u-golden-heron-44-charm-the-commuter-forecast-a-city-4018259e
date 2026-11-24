"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one line of weather for Pocketwick, a city that
# does not exist: scattered sunshine at 21 degrees, a 60% chance the
# bus actually shows up, and an umbrella with nothing to do. One line,
# 134 characters, inside the 140-character gate.
# Revision note: kept the forecast register and the bus joke; trimmed
# the closing clause so the line stays under 140 characters.
import os

TEXT = (
    "In Pocketwick today: scattered sunshine at 21\u00b0, a 60% chance "
    "your bus actually shows up, and zero chance your umbrella earns "
    "its keep."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
