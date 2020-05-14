import argparse
import shutil
from pathlib import Path


def capitalize_filename(path: Path) -> Path:
    filename = str(path.name).title()
    new_path = Path(path.parent, filename)
    return new_path


description = "A command-line tool to recursively capitalize all files in a directory. Use with CAUTION."

ap = argparse.ArgumentParser(description=description)
ap.add_argument(
    "-d",
    "--dir",
    required=True,
    help="Path to search recurively for filenames to capitalize.",
)
args = vars(ap.parse_args())


DIR = Path(argparse["dir"])
# Assumeme if a file is passed to just capitalize it
if DIR.is_file:
    new_path = capitalize_filename(DIR)
    shutil.move(DIR, new_path)
# Otherwise, recurisvely search for files.
elif DIR.is_dir:
    for i in DIR.rglob("*.*"):
        new_path = capitalize_filename(i)
        shutil.move(i, new_path)

        print(f"{i} -> {new_path}")
