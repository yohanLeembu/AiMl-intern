# Week 11 — Model Deployment Basics
### Handwritten Digit Classifier — Flask Demo App

This app deploys the neural network trained in the Week 10 mini-project (a
`scikit-learn` MLPClassifier trained on the `digits` dataset, ~96.7% test
accuracy) behind a small Flask web app. You draw a digit with your mouse in
the browser, and the app returns a live prediction.

> **Note on Streamlit vs Flask:** the assignment suggested Streamlit or
> Flask. This demo uses **Flask**, since that's what was available/installable
> in the environment this was built and tested in. Everything below (saving
> the model, loading it in a small app, taking user input, returning a
> prediction) is the same core deployment workflow either framework would use.

---

## What's in this folder

```
week11_app/
├── app.py              # Flask server: loads the model, exposes / and /predict
├── templates/
│   └── index.html      # Browser UI — a drawable canvas + JS to call the API
├── digit_model.pkl      # The trained neural network (pickled)
├── scaler.pkl            # The StandardScaler used on training data (pickled)
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## How it works (high level)

1. **`digit_model.pkl`** — the trained `MLPClassifier` from Week 10, saved
   with Python's `pickle` module so it doesn't need to be retrained every time
   the app starts.
2. **`scaler.pkl`** — the `StandardScaler` fit on the training data. This has
   to be saved and reused too — if you scale new input differently than the
   training data was scaled, predictions will be wrong. Saving *both* pieces
   together is the "proper" way to export this kind of model.
3. **`app.py`** loads both pickle files once when the server starts, then
   exposes:
   - `GET /` — serves the HTML page with the drawing canvas
   - `POST /predict` — accepts a base64 PNG image of the drawing, resizes it
     to 8x8 (matching the training data format), scales it with the saved
     scaler, and returns the model's predicted digit plus its top-3 guesses
     with confidence scores
   - `GET /health` — simple health check endpoint
4. **`templates/index.html`** — a canvas you draw on with your mouse/finger,
   plus a bit of JavaScript that captures the drawing as a PNG and sends it to
   `/predict`, then displays the result.

## How to run it locally

1. **Install dependencies** (ideally in a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the app:**
   ```bash
   python app.py
   ```
   You should see output like:
   ```
   * Running on http://127.0.0.1:5000
   ```

3. **Open your browser** to:
   ```
   http://127.0.0.1:5000
   ```

4. **Draw a digit** (0–9) on the black canvas with your mouse, then click
   **Predict**. The app will show the predicted digit and its top-3 guesses
   with confidence percentages. Click **Clear** to try another digit.

## Testing notes

Before sharing this app, it was tested end-to-end over real HTTP requests
(not just imported and called in Python): the running server was sent several
digit images and correctly classified all of them, confirming the full
pipeline — image in, prediction out — works as expected:

```
true=0  predicted=0  [OK]
true=7  predicted=7  [OK]
true=2  predicted=2  [OK]
true=5  predicted=5  [OK]
true=2  predicted=2  [OK]
true=1  predicted=1  [OK]

6/6 correct on this end-to-end HTTP test batch
```

Because the model was originally trained on small, clean 8x8 dataset images
rather than freehand mouse drawings, real hand-drawn digits (especially messy
or off-center ones) may be classified less reliably than the dataset's own
test images — that's expected, and is a good illustration of why real-world
deployment often needs extra care (e.g. better image preprocessing, more
training data) beyond what worked in the notebook.

## What I learned

- A trained model isn't useful to anyone else until it's **exported** in a
  reusable form — here, `pickle`, but `.pt` (PyTorch) or `.h5` (Keras) work
  the same way in spirit for other frameworks.
- **The preprocessing pipeline is part of the model.** The scaler had to be
  saved and reloaded exactly as used in training, or predictions would be
  silently wrong (a very common real-world deployment bug).
- Turning a notebook into "something others can use" is mostly about wrapping
  the same `predict()` call in a bit of app/server code, with a way to get
  input in and results out — the ML part barely changes.
- Testing the trained model against curated dataset images is not the same as
  testing it against messy, real-world input (like a mouse drawing) — a model
  that scores 96.7% on a clean test set can still struggle with inputs that
  look different from what it was trained on.
