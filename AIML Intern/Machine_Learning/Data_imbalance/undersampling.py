import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from collections import Counter
from imblearn.under_sampling import RandomUnderSampler

# Example dataset (you can replace this with your real data)
# For demonstration, let's create a dummy imbalanced dataset
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2,
                           weights=[0.9, 0.1], random_state=42)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Undersampling
rus = RandomUnderSampler(random_state=42)
X_under, y_under = rus.fit_resample(X_train, y_train)
print("After Undersampling:", Counter(y_under))

# Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_under, y_under)

# Predict and evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
