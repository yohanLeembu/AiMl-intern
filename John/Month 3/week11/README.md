# Week 11 — Model Deployment Basics
### Fashion-MNIST Classifier — Flask Demo App

This app deploys the CNN trained in the Week 10 mini-project (a small PyTorch
convolutional network trained on Fashion-MNIST, **91.39% test accuracy**)
behind a small Flask web app. You draw a clothing item with your mouse or
finger in the browser, and the app returns a live prediction with its top-3
guesses.

> **Note on Streamlit vs Flask:** the assignment suggested Streamlit or Flask.
> This demo uses **Flask**. The core deployment workflow (save the model, load
> it in a small app, take user input, return a prediction) is the same for
> either framework.

---

## What's in this folder

```
week11_app/
├── app.py              # Flask server: loads the model, exposes / and /predict
├── templates/
│   └── index.html      # Browser UI: a drawable canvas + JS that calls the API
├── fashion_cnn.pt      # Trained weights (YOU create this, see step 1 below)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Step 1 — Export the trained model from the notebook

The Week 10 notebook now ends with a **"9. Save the model"** section. Run the
whole notebook (or at least that last cell after training) and it writes
`fashion_cnn.pt`. On Kaggle, download it from the *Output* tab. Put it in this
folder next to `app.py`.

`fashion_cnn.pt` holds the model's `state_dict()`, which is just the learned
weights. `app.py` rebuilds the same layers (copied from the notebook) and loads
the weights into them. The last cell also reloads the file and checks the
predictions match the original model.

## Step 2 — Run it locally

1. **Install dependencies** (ideally in a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```
   If the PyTorch download is large, the CPU-only build is enough:
   ```bash
   pip install torch --index-url https://download.pytorch.org/whl/cpu
   ```

2. **Start the app:**
   ```bash
   python app.py
   ```
   You should see `Running on http://127.0.0.1:5000`.

3. **Open** `http://127.0.0.1:5000` in your browser.

4. **Draw an item** on the black canvas, then click **Predict**. Click
   **Clear** to try another one.

   Tips for better results: draw a **solid, filled-in** shape (the training
   images are filled silhouettes, not outlines) and make it big. Position
   doesn't matter because the app crops and centres your drawing.

## How it works

1. **`fashion_cnn.pt`** — the trained weights, saved so the model doesn't need
   to be retrained every time the app starts.
2. **`app.py`** builds the same network as the notebook, loads the weights once
   at startup, and calls `model.eval()`. It exposes:
   - `GET /` — serves the page with the drawing canvas
   - `POST /predict` — accepts a base64 PNG of the drawing, preprocesses it,
     runs the CNN, and returns the predicted class plus the top 3 guesses with
     confidence scores (softmax probabilities)
   - `GET /health` — simple health check
3. **Preprocessing** (`preprocess_canvas_image`) turns the canvas into what the
   model was trained on: a `(1, 1, 28, 28)` tensor of values 0–1, white item on
   a black background. Fashion-MNIST items are cropped tight and scaled so the
   longest side is 28 px, then centred, so the app does the same instead of a
   plain shrink of the whole canvas.
4. **`templates/index.html`** — the canvas, brush-size slider and the
   JavaScript that sends the drawing to `/predict` and shows the result.

## What changed compared with the Week 11 digits demo

| Digits demo (scikit-learn) | This demo (PyTorch) |
|---|---|
| `digit_model.pkl` + `scaler.pkl` (pickle) | `fashion_cnn.pt` (`state_dict`) |
| 8×8 images, values 0–16, `StandardScaler` | 28×28 images, values 0–1 (just ÷255), no scaler |
| Flat input `(1, 64)` | Image input `(1, 1, 28, 28)` |
| Classes are the digits 0–9 | Classes are the 10 clothing names |

The old `digit_model.pkl` and `scaler.pkl` are not used any more and can be deleted.

## Testing notes

This is what has been checked, and what has not:

- **Checked:** the Flask routes (`/`, `/health`, `/predict`), the JSON that comes
  back (top-3 sorted, labels matching indices), the error handling (blank
  canvas, tiny drawing, corrupt or missing image data, a missing `fashion_cnn.pt`),
  and the preprocessing (output is `(1, 1, 28, 28)` float32 in 0–1; tall and
  wide shapes are cropped to fill the frame and centred; transparent PNGs are
  handled). These ran with a stand-in for PyTorch, because it could not be
  installed where the app was built.
- **Not checked:** predictions from the real trained weights. Run the app with
  your own `fashion_cnn.pt` and try a few items before you demo it.

Expect imperfect results on drawings. The model scored 91.39% on the clean
Fashion-MNIST test set, but a mouse-drawn silhouette looks different from the
dataset's grayscale product photos, so some guesses will be wrong. Shirt vs
T-shirt vs pullover vs coat is the hardest group even on the real test set.

## What I learned

- A trained model isn't useful to anyone else until it's **exported**. For
  PyTorch the standard way is to save the `state_dict` (the weights) and rebuild
  the architecture in the app. For scikit-learn it was `pickle`.
- **The preprocessing pipeline is part of the model.** Training used pixels ÷
  255 in a `(1, 28, 28)` shape; the app must feed exactly that or predictions
  are silently wrong.
- `model.eval()` and `torch.no_grad()` matter when predicting.
- Testing on curated dataset images is not the same as testing on messy,
  real-world input, so a high test accuracy doesn't guarantee good results in
  the app.
