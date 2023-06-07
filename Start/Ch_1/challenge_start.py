# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json

# open the data file and load the JSON
with open("/workspaces/advanced-python-working-with-data-4312001/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
print("Total quakes: " + str(len(data["features"])))

# 2: How many quakes were felt by at least 100 people?
more_than_100 = sum(quake["properties"]["felt"] 
                    is not None and quake["properties"]
                    ["felt"] >= 100 for quake in data["features"])
print(f"Total quakes felt by at least 100 people: {more_than_100}")

# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def get_nb_felt(item):
    felt = item["properties"]["felt"]
    if felt is None:
        felt = 0
    return float(felt)

max_felt = max(data["features"], key=get_nb_felt)
print("Most felt reports: M " + str(max_felt["properties"]["mag"]) + " - " + max_felt["properties"]["place"] + ", reports: " + str(max_felt["properties"]["felt"]))

# 4: Print the top 10 most significant events, with the significance value of each
def most_sign(item):
    significant = item["properties"]["sig"]
    if significant is None:
        significant = 0
    return float(significant)

data["features"].sort(key=most_sign, reverse=True)
for i in range(10):
    print("Event: M " + 
          str(data["features"][i]["properties"]["mag"]) + 
          " - " + 
          data["features"][i]["properties"]["place"] + 
          ", Significance: " + 
          str(data["features"][i]["properties"]["sig"]))
