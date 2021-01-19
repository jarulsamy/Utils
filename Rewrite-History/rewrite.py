#!/usr/bin/python3

import argparse
import os
from datetime import datetime, timedelta
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

ENV_VARS = ["GIT_COMMITTER_DATE", "GIT_AUTHOR_DATE"]

if args["timestamp"] == "yesterday":
    date_ = datetime.today() - timedelta(days=1)
else:
    try:
        date_ = datetime.strptime(args["timestamp"], "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

time = datetime.now()
time = datetime.strftime(time, "%H:%M:%S")
date_time = f"{datetime.strftime(date_, '%Y-%m-%d')} {time}"

for i in ENV_VARS:
    os.environ[i] = date_time

print("Dropping you into a new shell session.")
print("Use exit to leave and unset the GIT variables.")

for i in ENV_VARS:
    os.system(f"echo {i}: ${i}")

os.system(args["shell"])
