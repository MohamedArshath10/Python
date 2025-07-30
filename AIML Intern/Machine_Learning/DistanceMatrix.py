from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# Input features (Hours studied)
X = np.array([[1], [2], [3], [4], [5], [6]])
# Labels: 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 1, 1, 1])

# Train-Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Predict
print("Predictions:", model.predict(X_test))
print("Accuracy:", model.score(X_test, y_test))