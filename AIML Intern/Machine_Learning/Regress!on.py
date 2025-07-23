from sklearn.linear_model import LinearRegression
import  numpy as np

x = np.array([[1], [2], [3], [4]])
y = np.array([4,8,12,16])
model = LinearRegression()
model.fit(x,y)
print("Intercept: ", model.intercept_)
print("Slope: ", model.coef_)
print("Predicted values: ", model.predict([[12]]))