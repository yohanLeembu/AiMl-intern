"""
Scam Message Detector - Flask demo app.
Paste a text message, get a verdict, a spam score and the words behind it.
"""

import os

import joblib
from flask import Flask, jsonify, render_template, request

import spamlib  # must be importable: the saved model refers to spamlib.normalize_text

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "scam_model.joblib")
MAX_CHARS = 2000

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        "models/scam_model.joblib not found. Run `python train.py` first "
        "(it needs data/spam.csv, see README)."
    )

bundle = joblib.load(MODEL_PATH)
# Looked up once at startup instead of on every request
FEATURE_NAMES = bundle["pipeline"].named_steps["tfidf"].get_feature_names_out()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    message = data.get("message")

    if not isinstance(message, str) or not message.strip():
        return jsonify({"error": "Paste a message to check."}), 400
    if len(message) > MAX_CHARS:
        return jsonify({"error": f"Message is too long (max {MAX_CHARS} characters)."}), 400

    try:
        result = spamlib.predict_message(bundle, message.strip(), FEATURE_NAMES)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    # localhost + debug off: debug mode on an open port lets others run code on your PC
    app.run(debug=False, host="127.0.0.1", port=5000)
