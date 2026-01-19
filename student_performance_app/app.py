from flask import Flask, render_template, request, jsonify
import joblib
from preprocess import preprocess_input

app = Flask(__name__)

# Load trained model
model = joblib.load("huber_regressor_model.pkl")

@app.route("/")
def home():
    return render_template("welcome.html")


@app.route("/predict-page")
def predict_page():
    return render_template("predict.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    processed_data = preprocess_input(data)

    prediction = model.predict(processed_data)[0]

    return jsonify({
        "prediction": round(float(prediction), 2)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=10000)
