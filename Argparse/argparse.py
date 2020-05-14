import argparse
from pprint import pprint

ap = argparse.ArgumentParser()

# Parameter arguments
ap.add_argument(
    "-a",
    "--longer_a",
    required=False,
    help="Some help",
    default="optional -> Some default",
)

# Flag arguments
ap.add_argument(
    "-d", "--debug", required=False, action="store_true", help="Toggle for debug mode."
)

args = vars(ap.parse_args())

pprint(args)
