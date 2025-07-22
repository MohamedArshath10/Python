from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
print(df.head())

# Splitting data
print("Splitting data ---->")
x = df.drop('target', axis=1)
y = df['target']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
print("Train size: ", x_train.shape)
print("Test size: ", x_test.shape)

# Decision tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

# Making Prediction
print("Making Prediction ---->")
y_pred = model.predict(x_test)
print(y_pred[:5])

# Evaluation Metrics
print("Final Evaluation ---->")
from sklearn.metrics import accuracy_score ,confusion_matrix, classification_report
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix \n",  confusion_matrix(y_test, y_pred))
print("Classification Report \n", classification_report(y_test, y_pred))
