from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load your trained model
model = joblib.load('path_to_your_trained_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract make and model from the request
        data = request.get_json()
        make = data['make']
        model_name = data['model']
        
        # Assuming your model takes these as inputs and outputs a prediction
        prediction = model.predict([[make, model_name]])  # Ensure your model's input is structured correctly
        
        # Return the prediction in JSON format
        return jsonify({'prediction': float(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
