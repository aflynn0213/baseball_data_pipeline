import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the trained model
model = joblib.load('models/trained_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])  # Assuming input is a list of features
    return jsonify({'prediction': prediction.tolist()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050)  # Port where the app will run
