"""
Shared helpers for the scam / spam message detector.

Used by train.py, the notebook and the Flask app, so the exact same
cleaning, text preprocessing and explanation code runs everywhere.
"""

import csv
import re
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

RANDOM_STATE = 42

# Patterns that are strong scam signals but get lost by a plain word model
URL_RE = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)
CURRENCY_RE = re.compile(r"[£$€]")
LONG_NUMBER_RE = re.compile(r"\b\d{5,}\b")   # phone numbers, short codes, account numbers

# Readable names for the special tokens, used when explaining predictions
FRIENDLY = {
    "urltoken": "[link]",
    "currencytoken": "[money symbol]",
    "numbertoken": "[long number]",
}


# ----------------------------------------------------------------------------
# Loading and cleaning
# ----------------------------------------------------------------------------
def load_data(path):
    """
    Load the SMS Spam Collection and return a DataFrame with columns
    'label' (ham/spam) and 'text'.

    Handles the Kaggle version (spam.csv: columns v1, v2 + empty extra columns,
    latin-1 encoded) and the original UCI file (tab separated, no header).
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {path}. Download 'SMS Spam Collection Dataset' "
            "from Kaggle and save it as data/spam.csv (see README)."
        )

    if path.suffix.lower() == ".csv":
        raw = pd.read_csv(path, encoding="latin-1")
        if {"v1", "v2"}.issubset(raw.columns):
            df = raw[["v1", "v2"]]
        else:
            df = raw.iloc[:, :2]
    else:  # original UCI file: label <TAB> message
        raw = pd.read_csv(path, sep="\t", header=None, quoting=csv.QUOTE_NONE,
                          encoding="latin-1")
        df = raw.iloc[:, :2]

    df = df.copy()
    df.columns = ["label", "text"]
    return df


def clean_data(df):
    """
    Clean the raw data. Returns (clean_df, log) where log counts what was removed.

    Duplicates are removed *before* the train/test split on purpose: if the same
    message sat in both sets the test score would be inflated (data leakage).
    """
    log = {"rows_loaded": int(len(df))}

    df = df.dropna(subset=["label", "text"]).copy()
    df["label"] = df["label"].astype(str).str.strip().str.lower()
    df["text"] = df["text"].astype(str).str.strip()
    df = df[df["label"].isin(["ham", "spam"]) & (df["text"] != "")].copy()
    log["rows_after_dropping_bad_rows"] = int(len(df))

    before = len(df)
    df = df.drop_duplicates().copy()
    log["exact_duplicates_removed"] = int(before - len(df))

    # Same text with two different labels is ambiguous, so drop all of those rows
    conflicting = df.duplicated("text", keep=False)
    log["conflicting_label_rows_removed"] = int(conflicting.sum())
    df = df[~conflicting].copy()

    df["label_num"] = (df["label"] == "spam").astype(int)   # spam = 1 (the class we care about)
    df = df.reset_index(drop=True)
    log["rows_final"] = int(len(df))
    return df, log


# ----------------------------------------------------------------------------
# Text preprocessing and model
# ----------------------------------------------------------------------------
def normalize_text(text):
    """
    Lowercase, then replace links, money symbols and long numbers with
    placeholder words. 'win 09061701461 at www.x.com' and 'win 07123456789 at
    www.y.com' then look the same to the model, which is what we want.
    """
    text = str(text).lower()
    text = URL_RE.sub(" urltoken ", text)
    text = CURRENCY_RE.sub(" currencytoken ", text)
    text = LONG_NUMBER_RE.sub(" numbertoken ", text)
    return text


def build_pipeline(classifier):
    """TF-IDF on words and word pairs, followed by a classifier."""
    return Pipeline([
        ("tfidf", TfidfVectorizer(preprocessor=normalize_text, ngram_range=(1, 2),
                                  min_df=2, sublinear_tf=True)),
        ("clf", classifier),
    ])


def candidate_models():
    """The models compared in the project (same features, different classifier)."""
    return {
        "Naive Bayes": MultinomialNB(alpha=0.1),
        "Logistic Regression": LogisticRegression(C=10, class_weight="balanced", max_iter=1000),
        "Linear SVM": LinearSVC(C=1.0, class_weight="balanced"),
    }


# ----------------------------------------------------------------------------
# Predicting and explaining
# ----------------------------------------------------------------------------
def pretty_term(term):
    for raw, nice in FRIENDLY.items():
        term = term.replace(raw, nice)
    return term


def explain(pipeline, text, feature_names=None, top_n=5):
    """
    Which words pushed this message towards 'spam' or 'safe'?

    Logistic regression adds up (word weight x TF-IDF value) for every word in
    the message, so each word's share of that sum is its contribution.
    Returns (spam_signals, safe_signals), each a list of (term, contribution).
    """
    vec = pipeline.named_steps["tfidf"]
    clf = pipeline.named_steps["clf"]
    if feature_names is None:
        feature_names = vec.get_feature_names_out()

    x = vec.transform([text]).tocsr()
    contrib = x.data * clf.coef_[0][x.indices]
    order = np.argsort(contrib)

    spam = [(pretty_term(feature_names[x.indices[i]]), float(contrib[i]))
            for i in order[::-1] if contrib[i] > 0][:top_n]
    safe = [(pretty_term(feature_names[x.indices[i]]), float(contrib[i]))
            for i in order if contrib[i] < 0][:top_n]
    return spam, safe


def predict_message(bundle, text, feature_names=None, top_n=5):
    """Score one message with the saved model bundle and explain the result."""
    pipeline = bundle["pipeline"]
    threshold = bundle["threshold"]
    score = float(pipeline.predict_proba([text])[0, 1])
    spam_signals, safe_signals = explain(pipeline, text, feature_names, top_n)
    return {
        "is_scam": score >= threshold,
        "score": score,
        "threshold": threshold,
        "spam_signals": [{"term": t, "weight": round(w, 3)} for t, w in spam_signals],
        "safe_signals": [{"term": t, "weight": round(w, 3)} for t, w in safe_signals],
    }
