"""Write this entry's poem for make.fun's "The poem about stopping" bounty.

The poem lives in entry.txt beside this file. This program copies its bytes,
unchanged, to the entry file the grader reads: <MAKEFUN_OUTPUT_DIR>/entry.txt.
"""

import os
from pathlib import Path

def entry_path() -> Path:
    """The poem, kept beside this program."""
    return Path(__file__).resolve().parent / "entry.txt"


def output_path() -> Path:
    """Where the grader reads the entry, inside MAKEFUN_OUTPUT_DIR."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    """Copy the poem byte for byte to the grader's entry file."""
    text = entry_path().read_bytes()
    destination = output_path()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(text)


if __name__ == "__main__":
    main()
