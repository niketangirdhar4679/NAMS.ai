import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load crash data
data = pd.read_csv('data/crash_data.csv')

# Feature engineering and data preparation
X = data[['weather', 'traffic_conditions', 'road_type', 'time_of_day']]
y = data['accident_severity']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model creation
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Model evaluation
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the model
import joblib
joblib.dump(model, 'models/accident_prediction_model.pkl')
