import pandas as pd
import joblib

# load scaler
scaler = joblib.load("scaler.pkl")

def preprocess_input(data):
    """
    data: dictionary from frontend
    """

    df = pd.DataFrame([{
        "Hours Studied": float(data["hours"]),
        "Previous Scores": float(data["previous_score"]),
        "Extracurricular Activities": 1 if data["activity"] == "Yes" else 0,
        "Sleep Hours": float(data["sleep"]),
        "Sample Question Papers Practiced": float(data["papers"])
    }])

    scaled_data = scaler.transform(df)
    return scaled_data
