import folium
import pandas as pd
import geopandas as gpd

# Load the data (example data, use your cleaned and processed dataset)
geo_data = gpd.read_file('data/VICTORIAN_ROAD_CRASH_DATA.geojson')

# Add some prediction logic or use the model output to assign risk levels
# For this example, we assign random risk levels
import numpy as np
np.random.seed(42)  # For reproducibility
geo_data['predicted_risk'] = np.random.rand(len(geo_data))

# Initialize a Folium map centered on Victoria
map_victoria = folium.Map(location=[-37.4713, 144.7852], zoom_start=7)

# Function to color markers based on risk level
def get_marker_color(risk_level):
    if risk_level > 0.75:
        return 'red'
    elif risk_level > 0.5:
        return 'orange'
    else:
        return 'green'

# Add markers for each accident hotspot
for _, row in geo_data.iterrows():
    if row['predicted_risk'] > 0.5:  # Show only higher risk areas
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=f"Risk Level: {row['predicted_risk']:.2f}",
            icon=folium.Icon(color=get_marker_color(row['predicted_risk']))
        ).add_to(map_victoria)

# Save the map as an HTML file
map_victoria.save('crash_hotspots_map.html')

print("Map saved as crash_hotspots_map.html")
