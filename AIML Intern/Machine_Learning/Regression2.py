from sklearn.linear_model import LinearRegression
import  numpy as np

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([30000, 35000, 40000, 45000, 50000])
model = LinearRegression()
model.fit(x,y)

print("Predicted values: ", model.predict([[6]]))