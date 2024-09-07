from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_accident_model(df):
    X = df[['traffic_volume', 'weather', 'road_type']]
    y = df['accident_severity']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    return model

# Model training
# model = train_accident_model(preprocessed_crash_data)
