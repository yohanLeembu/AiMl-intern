# %% [markdown]
# # Week 4 — vectors, dot products, and matrices
# Runnable examples to go with the concepts. Each `# %%` block is a
# separate cell in VS Code (Python extension) — click "Run Cell" above
# any block, or just run the whole file top to bottom.

# %%
import numpy as np

# %% [markdown]
# ## Vectors
# A vector is an arrow: direction + magnitude.

# %%
a = np.array([3, 4])
print("vector a:", a)
print("magnitude:", np.linalg.norm(a))

# %% [markdown]
# ## Dot product
# Multiply matching components, then sum. Measures how much two
# vectors point the same way: positive = aligned, zero = perpendicular,
# negative = opposite.

# %%
a = np.array([1, 2])
b = np.array([3, 4])

print("manual:", a[0] * b[0] + a[1] * b[1])
print("numpy:", np.dot(a, b))  # same as a @ b

# %%
same_dir = (np.array([1, 0]), np.array([2, 0]))
perpendicular = (np.array([1, 0]), np.array([0, 1]))
opposite = (np.array([1, 0]), np.array([-1, 0]))

for v1, v2 in [same_dir, perpendicular, opposite]:
    print(f"{v1} . {v2} = {np.dot(v1, v2)}")

# %% [markdown]
# ## Cosine similarity
# Dot product normalized by both magnitudes — this is what your RAG
# pipeline used to rank documents against a query embedding.

# %%
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

query = np.array([0.8, 0.6])
doc_a = np.array([0.9, 0.5])
doc_b = np.array([-0.6, 0.8])

print("query vs doc_a:", cosine_similarity(query, doc_a))
print("query vs doc_b:", cosine_similarity(query, doc_b))

# %% [markdown]
# ## Matrices
# A grid of numbers — or a machine that transforms vectors.

# %%
M = np.array([[1, 0],
              [0, -1]])
print("M:\n", M)

# %% [markdown]
# ## Matrix multiplication
# Each output value is the dot product of one row of the matrix with
# the input vector.

# %%
v = np.array([3, 4])
print("M @ v =", M @ v)  # flips the y-coordinate

# %% [markdown]
# ## A neural net layer
# weights (matrix) @ input (vector) + bias — this is what every layer
# does. "Training" is adjusting the numbers inside `weights`.

# %%
weights = np.array([[0.2, 0.8],
                     [0.5, -0.3]])
bias = np.array([0.1, -0.1])
input_vector = np.array([1.0, 2.0])

output = weights @ input_vector + bias
print("layer output:", output)
