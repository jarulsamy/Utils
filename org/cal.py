#!/usr/bin/env python3
"""
Convert malformed calendar entries into Org-Agenda TODO items.

Usage:
    1. Export Canvas calendar to Google Calendar.
    2. Export Google Calendar to ICS.
    3. Load ICS into Emacs iCal.
    4. Pipe contents of Emacs iCal schedule into this script. (cat school_schedule.org | ./cal.py > physics.org)
    5. Profit?

I wrote all the regex for this without looking at documentation.
"""
import datetime
import re
import sys
from collections import defaultdict

# use stdin if it's full
if not sys.stdin.isatty():
    input_stream = sys.stdin
# otherwise, read the given filename
else:
    try:
        input_filename = sys.argv[1]
    except IndexError:
        message = "need filename as first argument if stdin is not full"
        raise IndexError(message)
    else:
        input_stream = open(input_filename, "r")

pattern = re.compile(r"^%%\(and \(diary-block ([\d\s]+)\)\)(.+)")
SCHEDULED_TIME_FMT = "%Y-%m-%d %a"
SCHEUDLED_TIME_STR = "DEADLINE: <{0} 23:59:00>"
entries = defaultdict(lambda: defaultdict(list))

for line in input_stream:
    for date, title in re.findall(pattern, line):
        try:
            date = date.split(" ")
            start_date, end_date = date[:3], date[3:]
        except IndexError:
            print(
                f"Skipping malformed entry: {date}, {title}",
                file=sys.stderr,
            )
            continue
        if start_date != end_date:
            print(
                f"Skipping due to mismatched start and end date: {title}",
                file=sys.stderr,
            )
            continue

        start_date = [int(i) for i in start_date]
        date_obj = datetime.date(start_date[2], start_date[0], start_date[1])
        if date_obj < datetime.date.today() - datetime.timedelta(days=1):
            continue

        scheduled_date = date_obj.strftime(SCHEDULED_TIME_FMT)

        title = title.strip()
        class_ = re.findall(r"\[.+\((.+)\)\]", title)
        try:
            class_ = class_[0]
        except IndexError:
            print(
                f"Skipping malformed entry: {date}, {title}",
                file=sys.stderr,
            )
            continue

        entry_text = f"* TODO {title}\n{SCHEUDLED_TIME_STR.format(scheduled_date)}"
        entries[class_][date_obj].append(entry_text)


for class_ in entries:
    for date, texts in sorted(entries[class_].items()):
        for i in texts:
            print(i)
