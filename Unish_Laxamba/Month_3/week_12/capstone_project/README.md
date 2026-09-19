# Capstone Project — Breast Cancer Diagnosis Classifier

**Week 12 capstone: a complete pipeline — data → cleaning → EDA → modeling →
evaluation → deployment — built end-to-end from what was learned across the
internship.**

> ⚠️ **This is a learning exercise on a public benchmark dataset — not a
> medically validated tool.** It should never be used for real diagnostic
> decisions.

---

## Problem statement

Given a set of measurements taken from a digitized image of a breast mass's
cell nuclei (radius, texture, concavity, symmetry, etc.), predict whether the
mass is **malignant** or **benign**. This is a binary classification problem
using the **Breast Cancer Wisconsin (Diagnostic)** dataset — 569 samples, 30
numeric features, bundled with scikit-learn.

**Why this problem was chosen:** it's realistic enough to require every step
of a real pipeline (meaningful EDA, real evaluation trade-offs, a natural
deployment story) while staying small enough to build, evaluate, and explain
clearly in the time available — and the domain makes "why does evaluation
metric choice matter" a very concrete conversation (a missed malignant case
is far worse than a false alarm).

*(As specified in the assignment, this problem should be run past a mentor
for sign-off before being treated as final — see "Next steps" below.)*

## Approach

1. **Data** — loaded the built-in `sklearn.datasets.load_breast_cancer()`
   dataset.
2. **Cleaning** — checked for missing values, duplicate rows, and sane dtypes
   (found none — the data was already clean — and checked class balance,
   which was mildly imbalanced: 357 benign vs. 212 malignant).
3. **EDA** — class balance chart, a correlation heatmap across the "mean"
   features, and per-class distribution plots for several key features to
   sanity-check that they actually separate the two classes.
4. **Modeling** — trained and compared three model types on the same
   train/test split: **Logistic Regression**, **Random Forest**, and a small
   **Neural Network (MLPClassifier)**.
5. **Evaluation** — accuracy, precision, recall, F1, and ROC-AUC for all
   three, plus a confusion matrix and feature-importance chart for the
   winner.
6. **Deployment** — packaged the winning model (plus a simplified 8-feature
   version for a usable demo form) behind a small **Flask app** with a web
   form, tested end-to-end over real HTTP requests.

## Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| **Logistic Regression** (final) | **0.9825** | 0.9861 | 0.9861 | **0.9861** | **0.9954** |
| Random Forest | 0.9561 | 0.9589 | 0.9722 | 0.9655 | 0.9932 |
| Neural Network (MLP) | 0.9561 | 0.9855 | 0.9444 | 0.9645 | 0.9921 |
| Deployment demo model (8 features only) | 0.9649 | — | — | 0.9726 | — |

**Logistic Regression won** — it had the best F1 and ROC-AUC *and* is the
simplest, most interpretable of the three. In this case, the simplest model
was also the best one, which is itself a useful takeaway: more complex
models (Random Forest, a neural net) don't automatically win, especially on
a modest-sized, mostly-linearly-separable dataset like this one.

The most influential features (by logistic regression coefficient) were
`worst texture`, `radius error`, `worst concave points`, `worst area`, and
`worst radius` — all consistent with the domain intuition that larger,
more irregular, more textured cell measurements indicate malignancy.

Full charts, code, and narrative are in
[`notebooks/capstone_analysis.ipynb`](notebooks/capstone_analysis.ipynb).

## What I'd improve with more time

- Get a domain expert / mentor's take on which 8 features are clinically
  sensible to simplify to for the demo, rather than picking purely by
  coefficient size.
- Handle the class imbalance more deliberately (class weights or
  resampling) and report malignant-class recall as the headline metric,
  since a missed malignant case is the costliest error type here.
- Add a calibration check on the predicted probabilities — a diagnostic-
  adjacent model's confidence scores should actually mean what they say.
- Harden the demo app with input validation and a production WSGI server
  before it's shown to anyone beyond a local demo.
- Compare model *families* against an explicit feature-engineering /
  dimensionality-reduction baseline (e.g. PCA), not just raw features.

## Repository structure

```
capstone_project/
├── README.md                          # this file
├── REFLECTION.md                       # internship reflection
├── notebooks/
│   └── capstone_analysis.ipynb         # full pipeline: EDA, modeling, evaluation
├── images/                              # exported charts (also embedded in the notebook)
├── app/                                  # Flask deployment demo
│   ├── app.py
│   ├── templates/index.html
│   ├── cancer_model.pkl                 # full 30-feature model (analysis)
│   ├── scaler.pkl                        # scaler for the 30-feature model
│   ├── demo_model_8feat.pkl              # simplified demo model (deployment)
│   ├── demo_scaler_8feat.pkl              # scaler for the demo model
│   ├── feature_names.pkl
│   ├── top_features.json
│   └── requirements.txt
└── presentation/
    └── capstone_presentation.pptx        # slide deck for the mentor/team walkthrough
```

## How to run the demo app

```bash
cd app
pip install -r requirements.txt
python app.py
```
Then open **http://127.0.0.1:5001** in a browser, fill in the 8 measurement
fields (sensible defaults are pre-filled), and click Predict.

This was tested end-to-end with real HTTP requests against several actual
dataset rows before being called done — 7/7 correct in that test batch.

## Next steps

- **Bring the problem statement and this write-up to a mentor for sign-off**,
  per the assignment — ideally before or shortly after this build, so any
  requested changes in scope or approach can still be made.
- Use `presentation/capstone_presentation.pptx` for the 10–15 minute
  walkthrough with the mentor/team.
- See `REFLECTION.md` for the internship-wide reflection.
