# Internship Reflection — Weeks 1–12

> **Note:** this is drafted from the actual work done across the Week 9–12
> mini-projects (deep learning basics, deployment, and this capstone), as a
> starting point. It's written in first person so it's ready to use, but you
> should personalize it — swap in your own genuine takeaways, specific
> moments, and struggles — before sharing it with your mentor. A reflection
> that isn't really yours won't be as useful to you later.

## 3 biggest things I learned this internship

1. **The pipeline matters more than any single model.**
   Across the digit classifier, the Flask deployments, and this capstone, the
   actual modeling code was a small fraction of the total work. Cleaning,
   choosing the right evaluation metrics, and making a trained model usable
   by someone else took at least as much thought as picking or tuning an
   algorithm — and skipping any one of those steps would have made the
   "accuracy number" meaningless or the project unusable.

2. **A higher-accuracy model isn't automatically the better choice.**
   In the capstone, a simple Logistic Regression beat both a Random Forest
   and a small neural network — and even where a more complex model wins,
   interpretability, training cost, and ease of deployment are real factors,
   not afterthoughts. I came in assuming "fancier model = better"; that
   wasn't true here.

3. **Deployment exposes assumptions that a notebook hides.**
   Getting a model into a Flask app surfaced problems that never showed up
   during training — e.g. needing to save the *scaler*, not just the model,
   and realizing that 30 raw input fields would make a demo unusable.
   Building something end-to-end, not just training a model, is what
   actually taught me this.

## 1–2 areas I want to keep improving

1. **Evaluation rigor on imbalanced or high-stakes problems.** I used
   standard metrics (accuracy, F1, ROC-AUC) throughout, but a problem like
   the capstone's medical framing deserves more — calibration checks,
   explicit cost-sensitive thresholds, and treating recall on the critical
   class as the headline number rather than one line in a report.

2. **Taking ownership of deployment robustness**, not just getting a demo
   working. My Flask apps work for a clean, well-behaved demo but don't yet
   handle bad input, errors, or production concerns — that's the natural
   next skill to build.

---

*Personalize this before sharing: what was the hardest bug you hit, what
surprised you most, and what would you tell yourself starting Week 1?*
