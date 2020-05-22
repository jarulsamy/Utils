#!/usr/bin/python3

import argparse
import os
from datetime import datetime
from datetime import date
from datetime import timedelta

ap = argparse.ArgumentParser()

ap.add_argument(
    "-t",
    "--timestamp",
    required=False,
    help="An optional custom timestamp.",
    default="yesterday"
)

args = vars(ap.parse_args())

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

print("Dropping you into a bash session.")
print("Use exit to leave and unset the GIT variables.")

for i in ENV_VARS:
    os.system(f"echo {i}: ${i}")

os.system("/bin/bash")
