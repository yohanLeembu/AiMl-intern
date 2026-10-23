"""
Capstone Project - Model Deployment
A minimal Flask app that loads the simplified 8-feature Logistic Regression
model and lets a user enter cell measurements to get a live diagnosis prediction.

NOTE: This is a learning-exercise demo on a public benchmark dataset
(Breast Cancer Wisconsin Diagnostic). It is not a validated medical tool.
"""

import json
import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

with open("demo_model_8feat.pkl", "rb") as f:
    model = pickle.load(f)

with open("demo_scaler_8feat.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("top_features.json") as f:
    feature_meta = json.load(f)

FEATURES = feature_meta["top8"]  # order must match training order


@app.route("/")
def index():
    # Pass feature metadata to the template so it can render sensible
    # input ranges/defaults for each field
    fields = []
    for name in FEATURES:
        fields.append({
            "name": name,
            "mean": round(feature_meta["means"][name], 3),
            "min": round(feature_meta["mins"][name], 3),
            "max": round(feature_meta["maxs"][name], 3),
        })
    return render_template("index.html", fields=fields)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    try:
        # Build the feature vector in the exact order the model was trained on
        values = [float(data["values"][name]) for name in FEATURES]
        X = np.array(values).reshape(1, -1)
        X_scaled = scaler.transform(X)

        pred = int(model.predict(X_scaled)[0])
        proba = model.predict_proba(X_scaled)[0]
        label = "benign" if pred == 1 else "malignant"

        return jsonify({
            "prediction": label,
            "confidence_benign": float(proba[1]),
            "confidence_malignant": float(proba[0]),
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001, use_reloader=False)
