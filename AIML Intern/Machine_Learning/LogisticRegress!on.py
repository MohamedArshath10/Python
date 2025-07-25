from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([0,1,0,1,0])

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

# Logistic regression model
model = LogisticRegression()
model.fit(x_train, y_train)

# Prediction
predictions = model.predict([[6]])
print("Prediction of 3 hours studied: ", predictions)