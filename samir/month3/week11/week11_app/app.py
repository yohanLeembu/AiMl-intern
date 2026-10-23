"""
Week 11 - Model Deployment Basics
A minimal Flask app that loads the Week 10 trained digit-classifier model
and lets a user draw a digit in the browser to get a live prediction.
"""

import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
from PIL import Image
import io
import base64

app = Flask(__name__)

# --- Load the trained model + scaler once at startup ---
with open("digit_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)


def preprocess_canvas_image(image_data_url: str) -> np.ndarray:
    """
    Takes a base64 PNG data URL from the HTML canvas (drawn in white-on-black,
    roughly matching the training data's style), resizes it down to 8x8 to
    match the scikit-learn 'digits' dataset format, and scales pixel values
    to the 0-16 range used during training.
    """
    header, encoded = image_data_url.split(",", 1)
    img_bytes = base64.b64decode(encoded)
    img = Image.open(io.BytesIO(img_bytes)).convert("L")  # grayscale

    # Resize to 8x8, same shape as the training images
    img = img.resize((8, 8), Image.LANCZOS)
    arr = np.array(img).astype(float)

    # Canvas drawing is white strokes (255) on black (0) background, same
    # polarity as the training images (bright pixel = ink). Scale 0-255 -> 0-16.
    arr = (arr / 255.0) * 16.0
    return arr.flatten().reshape(1, -1)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    image_data_url = data.get("image")
    if not image_data_url:
        return jsonify({"error": "No image provided"}), 400

    try:
        features = preprocess_canvas_image(image_data_url)
        features_scaled = scaler.transform(features)

        prediction = int(model.predict(features_scaled)[0])
        probabilities = model.predict_proba(features_scaled)[0]

        top3_idx = np.argsort(probabilities)[::-1][:3]
        top3 = [{"digit": int(i), "confidence": float(probabilities[i])} for i in top3_idx]

        return jsonify({"prediction": prediction, "top3": top3})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    # debug=True is handy while developing locally; set to False for a demo/deploy
    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=False)
