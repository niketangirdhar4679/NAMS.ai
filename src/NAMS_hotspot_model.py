import pandas as pd
import geopandas as gpd
from sklearn.ensemble import RandomForestClassifier
from shapely.geometry import Point

# Load cleaned data and geojson for spatial analysis
data = pd.read_csv('cleaned_data.csv')
gdf = gpd.read_file('/mnt/data/VICTORIAN_ROAD_CRASH_DATA.geojson')

# Create features for prediction (e.g., traffic count, road surface, weather conditions)
X = data[['TRAFFIC_COUNT', 'ROAD_SURFACE', 'ATMOSPHERIC_COND']]
y = data['CRASH_SEVERITY']

# Train a RandomForestClassifier model
model = RandomForestClassifier()
model.fit(X, y)

# Predict crash hotspots
gdf['predicted_risk'] = model.predict(gdf[['TRAFFIC_COUNT', 'ROAD_SURFACE', 'ATMOSPHERIC_COND']])

# Visualize crash hotspots using Folium or other mapping tools
gdf.to_file('predicted_hotspots.geojson')
