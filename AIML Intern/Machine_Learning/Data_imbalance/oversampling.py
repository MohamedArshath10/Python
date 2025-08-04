from sklearn.datasets import make_classification
from imblearn.over_sampling import RandomOverSampler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from collections import Counter

# Create imbalanced dataset
X, y = make_classification(n_samples=1000, weights=[0.9, 0.1], random_state=42)
print("Before Oversampling:", Counter(y))

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Apply Random Oversampling
ros = RandomOverSampler()
X_res, y_res = ros.fit_resample(X_train, y_train)
print("After Oversampling:", Counter(y_res))

# Train model
model = LogisticRegression()
model.fit(X_res, y_res)
y_pred = model.predict(X_test)

# Evaluate
print(classification_report(y_test, y_pred))