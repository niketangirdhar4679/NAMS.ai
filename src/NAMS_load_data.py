import pandas as pd

def load_crash_data(filepath):
    return pd.read_csv(filepath)

def load_traffic_data(filepath):
    return pd.read_csv(filepath)

def load_permit_data(filepath):
    return pd.read_csv(filepath)

# Example usage:
# crash_data = load_crash_data('victoria_road_crash_data.csv')
