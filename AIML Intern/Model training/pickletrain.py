import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# Sample data
iris = load_iris()
X, y = iris.data, iris.target

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# --- Saving ---
with open("model_pickle.pkl", "wb") as file:
    pickle.dump(model, file)

# --- Loading ---
with open("model_pickle.pkl", "rb") as file:
    loaded_model = pickle.load(file)

# Test
print(loaded_model.predict([X[0]]))