# Scam Message Detector — Capstone Project

A model that reads a text message, says whether it looks like a scam, and shows
**which words** made it suspicious. Includes a small Flask web app for live checks.

## Problem statement

Scam texts (fake prizes, "call now" messages, suspicious links) trick people into
paying money or sharing details. Goal: classify a message as **scam (spam)** or
**normal (ham)**, and make the decision explainable so a person can see why.

## Data

SMS Spam Collection (Almeida, Gómez Hidalgo & Yamakami, 2011): about 5.5k real
text messages labelled `ham` or `spam`, roughly 13% spam. Save it as `data/spam.csv`
(see `data/README.md`).

## Approach

| Step | What was done |
|---|---|
| Cleaning | Dropped bad rows, removed exact duplicates and messages with conflicting labels. Done **before** the split to avoid data leakage |
| EDA | Class imbalance, length, capital-letter share, links / money symbols / long numbers, most common words per class |
| Features | Lowercase text; links, money symbols and long numbers replaced by placeholder words; TF-IDF on words and word pairs |
| Modelling | Naive Bayes, Logistic Regression, Linear SVM compared with 5-fold cross-validation (precision, recall, F1) |
| Final model | Logistic Regression (tuned `C`), chosen because its word weights make predictions explainable |
| Evaluation | One-time check on a held-out 20% test set: precision, recall, F1, confusion matrix, precision-recall curve, error analysis |
| Deployment | Flask app: paste a message, get a verdict, a scam score and the words behind it |

Accuracy alone is misleading here (about 87% of messages are normal), so the project
focuses on **precision** and **recall** for the scam class.

## Results

Run `python train.py`. It writes **`reports/results.md`** with the model comparison,
test-set metrics and confusion matrix from your own run.
Cleaning log: {'rows_loaded': 5572, 'rows_after_dropping_bad_rows': 5572, 'exact_duplicates_removed': 414, 'conflicting_label_rows_removed': 0, 'rows_final': 5158}
Final: 5158 messages, 12.4% spam
Train: 4126  Test: 1032
  Naive Bayes          precision=0.992 recall=0.916 f1=0.952
  Logistic Regression  precision=0.970 recall=0.926 f1=0.947
  Linear SVM           precision=0.980 recall=0.913 f1=0.944
Best C = 10 (cv f1 = 0.947)
Test set: {'accuracy': 0.989, 'precision': 0.961, 'recall': 0.953, 'f1': 0.957} | TN=899 FP=5 FN=6 TP=122
Top spam words: [long number], [money symbol], [link], call, call [long number], to [long number], reply, txt, text, free, mobile, tones, 150p, your, sms

Saved C:\Intern\aiml internship\John\Month 3\week12\scam-message-detector\models\scam_model.joblib
Saved C:\Intern\aiml internship\John\Month 3\week12\scam-message-detector\reports\results.md
  score=1.00 scam=True :: URGENT! You have won a 1000 prize. Call 0901234567
  score=0.01 scam=False :: Are we still meeting at 6 for dinner tonight?



## How to run

1. Put the dataset at `data/spam.csv`.
2. Install dependencies (a virtual environment is recommended):
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model (creates `models/scam_model.joblib` and `reports/results.md`):
   ```bash
   python train.py
   ```
4. Start the app and open http://127.0.0.1:5000 :
   ```bash
   python app.py
   ```
5. For the full walkthrough with charts, open `capstone_scam_detector.ipynb`

## Project structure

```
scam-message-detector/
├── README.md
├── requirements.txt
├── spamlib.py                      # cleaning, text preprocessing, explanation (shared)
├── train.py                        # full pipeline in one command
├── capstone_scam_detector.ipynb    # step-by-step notebook with EDA and charts
├── app.py                          # Flask server
├── templates/
│   └── index.html                  # web page (must stay inside "templates")
├── data/                           # put spam.csv here
├── models/                         # created by train.py
└── reports/                        # created by train.py
```

## Limitations

- **Old, narrow data:** the messages are from the 2000s and mostly UK. Modern scams
  (fake delivery notices, bank phishing, "wrong number" chats) look different, so many
  will be missed. The app shows a statistical guess, not a guarantee.
- **Fixed threshold:** the verdict uses a 0.5 cut-off. The right value depends on whether
  missing a scam or flagging a real message is the costlier mistake.
- **Explanations show correlation, not proof:** a word's weight reflects patterns in this
  dataset only.

## What I would improve with more time

- Add a modern smishing / phishing dataset and re-evaluate
- Choose the threshold deliberately from the precision-recall curve
- Add character n-grams to catch obfuscated words ("fr33", "w1n")
- Compare a small transformer model against the explainable baseline
- Log misclassified messages and retrain regularly


