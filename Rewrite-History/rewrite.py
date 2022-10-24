#!/usr/bin/env python3
"""
Rewrite git history specifying a specific timestamp for commits.

usage: rewrite.py [-h] [-t TIMESTAMP] [-s SHELL] [-c]

options:
  -h, --help            show this help message and exit
  -t TIMESTAMP, --timestamp TIMESTAMP
                        Custom timestamp.
  -s SHELL, --shell SHELL
                        Custom shell
  -c, --color           Enable color shell
"""

import argparse
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

ap = argparse.ArgumentParser()

ap.add_argument(
    "-t",
    "--timestamp",
    required=False,
    help="Custom timestamp.",
    default="yesterday",
)
ap.add_argument(
    "-s",
    "--shell",
    required=False,
    help="Custom shell",
    default="/bin/zsh",
)
ap.add_argument(
    "-c",
    "--color",
    required=False,
    action="store_true",
    help="Enable color shell",
)
args = vars(ap.parse_args())

args["shell"] = Path(args["shell"])
if not args["shell"].exists:
    raise OSError("Shell doesn't exist")
if not args["color"]:
    os.environ["TERM"] = "xterm-mono"

env_vars = ("GIT_COMMITTER_DATE", "GIT_AUTHOR_DATE")

if args["timestamp"] == "yesterday":
    date_ = datetime.today() - timedelta(days=1)
else:
    try:
        date_ = datetime.strptime(args["timestamp"], "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

# Timezone aware datetimes are hard...
# https://stackoverflow.com/a/25887393
utc_dt = datetime.now(timezone.utc)
dt = utc_dt.astimezone()

time_str = datetime.strftime(dt, "%H:%M:%S %z")
date_time = f"{datetime.strftime(date_, '%Y-%m-%d')} {time_str}"

for i in env_vars:
    os.environ[i] = date_time

print("Dropping you into a new shell session.")
print("Use exit to leave and unset the GIT variables.")

for i in env_vars:
    os.system(f"echo {i}: ${i}")

os.system(args["shell"])
