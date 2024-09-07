import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data on vehicle registration, public transport, and bike infrastructure
vehicles = pd.read_csv('data/vehicle_registration.csv')
public_transport = pd.read_csv('data/public_transport_usage.csv')
bike_infrastructure = pd.read_csv('data/bike_infrastructure.csv')

# Merge datasets
combined_data = vehicles.merge(public_transport, on='postcode').merge(bike_infrastructure, on='postcode')

# Analyze correlations
corr_matrix = combined_data.corr()

# Visualize correlations
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation between Vehicle Registration, Public Transport Usage, and Bike Infrastructure')
plt.show()
