import csv
import folium
from folium.plugins import MarkerCluster

filename = '30DaysMapChallenge/Day 01_Points/StudyArea POI.csv'
keys = ('name', 'latitude', 'longitude', 'type', 'address')
records = []

# Read data from the CSV file into our Python app
with open(filename, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        records.append({key: row[key] for key in keys})

print(records[0])

# Create a map with a different basemap (e.g., Stamen Terrain)
map = folium.Map(location=[31.239324, 121.478415], zoom_start=16, tiles='cartodbpositron')

# Create a dictionary to hold MarkerClusters for each type
marker_clusters = {}

# Prepare data for MarkerClusters with popups
for record in records:
    latitude = float(record['latitude'])
    longitude = float(record['longitude'])
    name = record['name']
    type_ = record['type']
    address = record['address']
    
    # Create a popup content with proper HTML formatting
    popup_content = f"""
    <div style="font-size: 14px;">
        <strong>Name:</strong> {name}<br>
        <strong>Type:</strong> {type_}<br>
        <strong>Address:</strong> {address}
    </div>
    """
    
    # If the type is not in the marker_clusters, create a new MarkerCluster
    if type_ not in marker_clusters:
        marker_clusters[type_] = MarkerCluster(name=type_, disable_clustering_at_zoom=20)  # Set the zoom level here
    
    # Add a marker to the corresponding MarkerCluster with custom popup size
    folium.Marker(
        location=(latitude, longitude),
        popup=folium.Popup(popup_content, max_width=300, min_width=200) 
    ).add_to(marker_clusters[type_])

# Add all MarkerClusters to the map
for mc in marker_clusters.values():
    map.add_child(mc)

# Add LayerControl to toggle different types
folium.LayerControl().add_to(map)

# Save the map as an HTML file
map.save('30DaysMapChallenge/Day 01_Points/ShanghaiPOIMap.html')