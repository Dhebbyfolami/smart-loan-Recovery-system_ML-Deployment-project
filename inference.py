# inference.py

import joblib
import numpy as np

def load_artifacts(model_path="model/loan_model.pkl"):
    artifacts = joblib.load(model_path)
    return artifacts["model"], artifacts["scaler"], artifacts["features"]

def predict(features: dict, model_path="model/loan_model.pkl"):
    model, scaler, feature_names = load_artifacts(model_path)

    x = np.array([features.get(f, 0) for f in feature_names]).reshape(1, -1)
    x_scaled = scaler.transform(x)

    prob = model.predict_proba(x_scaled)[0][1]
    high_risk = prob < 0.5

    return {"repayment_probability": float(prob), "high_risk": bool(high_risk)}
