# %% [markdown]
# # Practice 1 — Linear Regression from Scratch
# Goal: understand the cost function + gradient descent mechanics by coding
# them by hand (no sklearn) on a tiny, easy-to-reason-about toy dataset.

# %%
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

# %% [markdown]
# ## Toy dataset: hours studied -> exam score
# Roughly `score = 10 + 11 * hours`, plus noise.

# %%
hours = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8])
true_score = 10 + 11 * hours
score = true_score + np.random.normal(0, 5, size=hours.shape)

plt.scatter(hours, score)
plt.xlabel("Hours studied")
plt.ylabel("Exam score")
plt.title("Toy dataset: hours studied vs exam score")
plt.show()

# %% [markdown]
# ## Cost function (MSE)
# $J(\theta) = \frac{1}{2m}\sum (\hat{y} - y)^2$

# %%
def compute_cost(x, y, theta0, theta1):
    m = len(x)
    predictions = theta0 + theta1 * x
    return (1 / (2 * m)) * np.sum((predictions - y) ** 2)

# %% [markdown]
# ## Gradient descent
# Update both parameters a small step against the gradient, every iteration.

# %%
def gradient_descent(x, y, alpha=0.02, n_iters=1000):
    m = len(x)
    theta0, theta1 = 0.0, 0.0
    cost_history = []
    for _ in range(n_iters):
        predictions = theta0 + theta1 * x
        error = predictions - y
        grad0 = (1 / m) * np.sum(error)
        grad1 = (1 / m) * np.sum(error * x)
        theta0 -= alpha * grad0
        theta1 -= alpha * grad1
        cost_history.append(compute_cost(x, y, theta0, theta1))
    return theta0, theta1, cost_history

theta0, theta1, cost_history = gradient_descent(hours, score)
print(f"Learned:  score = {theta0:.2f} + {theta1:.2f} * hours")
print(f"(true underlying relationship was  score = 10 + 11 * hours)")

# %%
plt.plot(cost_history)
plt.xlabel("Iteration")
plt.ylabel("Cost J(theta)")
plt.title("Cost function convergence")
plt.show()

# %%
plt.scatter(hours, score, label="data")
plt.plot(hours, theta0 + theta1 * hours, color="red", linewidth=2, label="fitted line")
plt.xlabel("Hours studied")
plt.ylabel("Exam score")
plt.legend()
plt.title("Fitted regression line")
plt.show()

# %% [markdown]
# ## Sanity check
# Compare the hand-rolled gradient descent result against numpy's closed-form
# fit (`polyfit`) — they should land close to each other.

# %%
slope, intercept = np.polyfit(hours, score, deg=1)
print(f"np.polyfit (closed-form): slope={slope:.2f}, intercept={intercept:.2f}")
print(f"gradient descent:         slope={theta1:.2f}, intercept={theta0:.2f}")
