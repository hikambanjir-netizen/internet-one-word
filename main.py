"""The Internet in One Word — the whole internet, in a single word.

Feral: wild, unowned, and liable to bite — the one word the entire
internet earns, from its comment sections to its cat videos.
"""

LINE = "feral"

import os

try:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
except OSError:
    pass

print(LINE)
