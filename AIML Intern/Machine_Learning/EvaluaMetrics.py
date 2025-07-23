from sklearn.metrics import mean_absolute_error
# Mean Absolute Error
y_true = [3, 0.5, 2]
y_pred = [2.5, 0, 2]
print("MAS: ",mean_absolute_error(y_true, y_pred))

# Mean Squared error
from sklearn.metrics import mean_squared_error
print("MSE: ",mean_squared_error(y_true, y_pred))

# Root Mean Squared Error
import numpy as np
print("RMSE: ",np.sqrt(mean_squared_error(y_true, y_pred)))

# R2 Score
from sklearn.metrics import r2_score
print("R2 Score: ",r2_score(y_true, y_pred))


