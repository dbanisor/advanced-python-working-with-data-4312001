# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import defaultdict
from pprint import pprint


# open the data file and load the JSON
with open("/workspaces/advanced-python-working-with-data-4312001/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

events = defaultdict(int)
for event in data["features"]:
    events[event["properties"]["type"]] += 1

event_counter = defaultdict(int)

for k, v in events.items():
    print(f"{k}: {v}")
