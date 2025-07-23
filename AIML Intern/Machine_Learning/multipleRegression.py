import  pandas as  pd
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    'Hours' : [1,2,3,4,5],
    'Experiences' : [1,2,1,3,2],
    'Score' : [2,4,5,4,5],
})
x = data[['Hours', 'Experiences']]
y = data['Score']
model = LinearRegression()
model.fit(x,y)
print(model.intercept_)
print(model.coef_)
# new_data = pd.DataFrame([[6, 2]], columns=['Hours', 'Experiences'])
# print("Predicted values: ", model.predict(new_data))
print("Predicted values: ", int(model.predict([[6, 2]])))
