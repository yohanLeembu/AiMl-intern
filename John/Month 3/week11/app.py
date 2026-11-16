"""
Week 11 - Model Deployment Basics
A minimal Flask app that loads the Week 10 trained Fashion-MNIST CNN (PyTorch)
and lets a user draw a clothing item in the browser to get a live prediction.
"""

import base64
import io
import os

import numpy as np
import torch
import torch.nn as nn
from flask import Flask, jsonify, render_template, request
from PIL import Image

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "fashion_cnn.pt")

# Same order as the notebook (label 0 -> "T-shirt/top", ..., label 9 -> "Ankle boot")
CLASS_NAMES = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

IMG_SIZE = 28


def build_model() -> nn.Sequential:
    """
    The exact architecture from the Week 10 notebook (section 5).
    The saved file only holds the weights, so the layers must be rebuilt
    in the same order here before the weights can be loaded into them.
    """
    return nn.Sequential(
        nn.Conv2d(1, 32, kernel_size=3, padding=1),   # 28x28 -> 28x28
        nn.ReLU(),
        nn.MaxPool2d(2),                              # -> 14x14
        nn.Conv2d(32, 64, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2),                              # -> 7x7
        nn.Flatten(),                                 # 64*7*7 = 3136
        nn.Linear(64 * 7 * 7, 128),
        nn.ReLU(),
        nn.Linear(128, 10),                           # 10 classes
    )


# --- Load the trained weights once at startup (CPU is plenty for one image) ---
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        "fashion_cnn.pt not found next to app.py. Run the last cells of "
        "week10_fashion_mnist_classifier.ipynb (section 9) to create it, "
        "then copy it into this folder."
    )

model = build_model()
model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu", weights_only=True))
model.eval()  # turn off training-only behaviour; always do this before predicting


def preprocess_canvas_image(image_data_url: str) -> np.ndarray:
    """
    Takes a base64 PNG data URL from the HTML canvas (white drawing on a black
    background, the same polarity as Fashion-MNIST) and turns it into the
    tensor shape the model was trained on: (1, 1, 28, 28), floats in 0-1.

    Fashion-MNIST items are cropped tight and scaled so the longest side is
    28 px, then centred. A raw 280x280 -> 28x28 resize would leave a small
    drawing tiny and off-centre, so we mimic that cropping here.
    """
    if not isinstance(image_data_url, str) or "," not in image_data_url:
        raise ValueError("Invalid image data.")

    _, encoded = image_data_url.split(",", 1)
    try:
        img_bytes = base64.b64decode(encoded)
        img = Image.open(io.BytesIO(img_bytes))
        img.load()
    except Exception:
        raise ValueError("Could not read the image.")

    # Flatten any transparency onto black, then convert to grayscale
    img = img.convert("RGBA")
    background = Image.new("RGBA", img.size, (0, 0, 0, 255))
    gray = np.array(Image.alpha_composite(background, img).convert("L"))

    # Find the drawing (ignore faint noise)
    ink = gray > 20
    rows = np.where(ink.any(axis=1))[0]
    cols = np.where(ink.any(axis=0))[0]
    if rows.size == 0:
        raise ValueError("The canvas is empty - draw something first.")

    cropped = gray[rows[0]:rows[-1] + 1, cols[0]:cols[-1] + 1]
    h, w = cropped.shape
    if max(h, w) < 10:
        raise ValueError("The drawing is too small - draw a bigger shape.")

    # Scale so the longest side is 28 px, keeping the aspect ratio
    scale = IMG_SIZE / max(h, w)
    new_w = min(IMG_SIZE, max(1, round(w * scale)))
    new_h = min(IMG_SIZE, max(1, round(h * scale)))
    small = Image.fromarray(cropped).resize((new_w, new_h), Image.Resampling.LANCZOS)

    # Paste into the centre of a black 28x28 image
    canvas = Image.new("L", (IMG_SIZE, IMG_SIZE), 0)
    canvas.paste(small, ((IMG_SIZE - new_w) // 2, (IMG_SIZE - new_h) // 2))

    # Same scaling as training: 0-255 -> 0-1, shape (batch, channel, H, W)
    arr = np.asarray(canvas, dtype=np.float32) / 255.0
    return np.ascontiguousarray(arr.reshape(1, 1, IMG_SIZE, IMG_SIZE))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    image_data_url = data.get("image")
    if not image_data_url:
        return jsonify({"error": "No image provided"}), 400

    try:
        features = preprocess_canvas_image(image_data_url)

        with torch.no_grad():
            logits = model(torch.from_numpy(features))
            probabilities = torch.softmax(logits, dim=1)[0].numpy()

        top3_idx = np.argsort(probabilities)[::-1][:3]
        top3 = [
            {
                "index": int(i),
                "label": CLASS_NAMES[int(i)],
                "confidence": float(probabilities[i]),
            }
            for i in top3_idx
        ]

        return jsonify({
            "prediction": top3[0]["label"],
            "prediction_index": top3[0]["index"],
            "top3": top3,
        })
    except ValueError as e:          # bad / empty drawing -> the user's problem
        return jsonify({"error": str(e)}), 400
    except Exception as e:           # anything else -> server problem
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    # Bound to localhost with debug off: Flask's debug mode lets anyone who can
    # reach the port run code, so don't combine debug=True with host="0.0.0.0".
    app.run(debug=False, host="127.0.0.1", port=5000)
