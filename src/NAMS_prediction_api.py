from flask import Flask, request, jsonify
from models.accident_prediction import train_accident_model

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict(data['features'])
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
