import pandas as pd
from sklearn.preprocessing import LabelEncoder
data = {'Gender' : ['Male', 'Female'],}
df = pd.DataFrame(data)

le = LabelEncoder()
df['Gender_encode'] = le.fit_transform(df['Gender'])
print(df)

# one-hat
df = pd.DataFrame({'city' : ['Chennai', 'salem']})
df_encoded = pd.get_dummies(df, columns=['city'])
print(df_encoded)