from flask import Flask, request, jsonify, render_template
import joblib
from src.NAMS_hotspot_model import predict_hotspots
from src.NAMS_executive_brief import create_executive_brief
from src.NAMS_preventative_measures import suggest_preventative_measures
from src.NAMS_policy_recommendations import recommend_policies

app = Flask(__name__)

# Root route to verify the app is running
@app.route('/')
def index():
    return "Welcome to the Road Safety AI System!"

# Endpoint for predicting crash hotspots
@app.route('/predict_hotspots', methods=['POST'])
def predict_hotspot_route():
    try:
        data = request.get_json()  # Assuming input data is JSON format
        predicted_hotspots = predict_hotspots(data)
        return jsonify(predicted_hotspots)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint for generating an executive brief
@app.route('/create_brief', methods=['POST'])
def create_brief_route():
    try:
        data = request.get_json()  # Example input: high_risk_areas, factors
        brief = create_executive_brief(data)
        return jsonify({'executive_brief': brief})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint for suggesting preventative measures
@app.route('/suggest_measures', methods=['POST'])
def suggest_measures_route():
    try:
        hotspots = request.get_json().get('hotspots')  # Input: a list of hotspot data
        measures = suggest_preventative_measures(hotspots)
        return jsonify({'suggested_measures': measures})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint for recommending policy guidelines
@app.route('/recommend_policies', methods=['POST'])
def recommend_policies_route():
    try:
        analysis = request.get_json()  # Input: accident analysis data
        policies = recommend_policies(analysis)
        return jsonify({'policy_recommendations': policies})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_accident')
def predict_accident():
    model = joblib.load('models/accident_prediction_model.pkl')
    # Placeholder for prediction logic
    prediction = model.predict([[1, 0, 2, 1]])  # Example input
    return f"Predicted Accident Severity: {prediction[0]}"

if __name__ == '__main__':
    app.run(debug=True)
