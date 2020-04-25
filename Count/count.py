import argparse
from pathlib import Path

description = (
    "A command-line tool to recursively count the number of files in a directory."
)

ap = argparse.ArgumentParser(description=description)
ap.add_argument(
    "-d", "--dir", required=True, help="Path to search recurively for filenames.",
)
args = vars(ap.parse_args())

DIR = Path(args["dir"])

total = 0
if DIR.is_file:
    total = 1
elif DIR.is_dir:
    for f in DIR.rglob("*.*"):
        total += 1

print(f"TOTAL # OF FILES: {total}")
