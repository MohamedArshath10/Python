import pandas as pd
from sklearn.preprocessing import LabelEncoder
data = {'Gender' : ['Male', 'Female'],}
df = pd.DataFrame(data)

le = LabelEncoder()
df['Gender_encode'] = le.fit_transform(df['Gender'])
print(df)

# one-hot
print("One-Hot ----->")
df = pd.DataFrame({'city' : ['Chennai', 'salem']})
df_encoded = pd.get_dummies(df, columns=['city'])
print(df_encoded)

# Manual mapping
print("Manual mapping ----->")
df = pd.DataFrame({'Married' : ['Yes', 'No']})
df['Married_encoded'] = df['Married'].map({'Yes': 1, 'No': 0})
print(df)