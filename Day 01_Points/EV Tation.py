import csv
import folium.map
import folium
from folium.plugins import FastMarkerCluster

filename = '30DaysMapChallenge\Day 01_Points\Electric_Vehicle_Charging_Stations.csv'
keys =  ('Station Name', 'New Georeferenced Column')
records = []

# read data from the csv file into our python app
with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        records.append({key: row[key] for key in keys})

print(records[0])

for record in records:
    longitude, latitude = record['New Georeferenced Column'].split('(')[-1].split(')')[0].split()
    record['longitude'] = float(longitude)
    record['latitude'] = float(latitude)

print(records[0])

map = folium.Map(location=[41.5025,-72.6999],zoom_start=9)

latitudes = [a['latitude']for a in records]
longitudes = [a['longitude']for a in records]

FastMarkerCluster(data=list(zip(latitudes,longitudes))).add_to(map)

# for record in records:
#     coords = (record['latitude'],record['longitude'])
#     folium.Marker(coords,popup=record['Station Name']).add_to(map)

map
