import pandas as pd

# Load datasets
accident = pd.read_csv('/mnt/data/ACCIDENT.csv')
road_surface = pd.read_csv('/mnt/data/ROAD_SURFACE_COND.csv')
atmospheric = pd.read_csv('/mnt/data/ATMOSPHERIC_COND.csv')
vehicle = pd.read_csv('/mnt/data/VEHICLE.csv')
traffic_counts = pd.read_csv('/mnt/data/Traffic_Count_Locations.csv')

# Merge datasets based on common keys (e.g., location, date)
merged_data = pd.merge(accident, road_surface, on='ACCIDENT_NO')
merged_data = pd.merge(merged_data, atmospheric, on='ACCIDENT_NO')
merged_data = pd.merge(merged_data, vehicle, on='ACCIDENT_NO')

# Clean and preprocess data (handle missing values, drop irrelevant columns)
merged_data.dropna(inplace=True)

# Save cleaned data for further analysis
merged_data.to_csv('cleaned_data.csv', index=False)