from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LogisticRegression
import numpy as np

# Load the Iris dataset
X, y = load_iris(return_X_y=True)

# Create a logistic regression model
model = LogisticRegression(max_iter=1000)

# Define 5-Fold Cross-Validation
kfold = KFold(n_splits=5, shuffle=True, random_state=1)

# Perform Cross-Validation
scores = cross_val_score(model, X, y, cv=kfold)

# Output the scores
print("Fold Scores:", scores)
print("Mean Accuracy:", np.mean(scores))