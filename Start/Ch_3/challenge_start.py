# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
from pprint import pprint
import datetime


# open the data file and load the JSON
with open("/workspaces/advanced-python-working-with-data-4312001/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
def most_signif_40(item):
    most_sig = item["properties"]["sig"]
    if most_sig is None:
        most_sig = 0
    return float(most_sig)

def get_date(d):
    time_date = d["properties"]["time"]
    if time_date is not None:
        return time_date

data["features"].sort(key=most_signif_40, reverse=True)

for item in range(40):
    data["features"].sort(key=get_date, reverse=True)

    
header = ["Magnitude", "Place", "Felt Reports", "Date", "Google Map link"]
results = []
               
for i in range(40):
    magnitude = data["features"][i]["properties"]["mag"]
    place = data["features"][i]["properties"]["place"]
    felt_reports = data["features"][i]["properties"]["felt"]
    date = datetime.date.fromtimestamp(int(data["features"][i]["properties"]["time"])/1000).isoformat()
    longitude = "{:.3f}".format(data["features"][i]["geometry"]["coordinates"][1])
    latitude = "{:.3f}".format(data["features"][i]["geometry"]["coordinates"][0])
    map_link = "https://www.google.com/maps/place/" + longitude + "," + latitude

    results.append([magnitude, place, felt_reports, date, map_link])


pprint(results)

# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

with open("/workspaces/advanced-python-working-with-data-4312001/significantevents.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(results)
