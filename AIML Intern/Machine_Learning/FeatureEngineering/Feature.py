import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.decomposition import PCA

data = pd.DataFrame({
    'Height': [150, 160, 170, 180],
    'Weight': [50, 65, 80, 95],
    'Age': [20, 25, 30, 35],
    'Gender': ['Male', 'Female', 'Female', 'Male'],
    'Income': [30000, 40000, 50000, 60000]
})
print("Original Data:\n", data)

data['BMI'] = data['Weight'] / (data['Height']/100)**2
data['Is_Adult'] = data['Age'].apply(lambda x: 1 if x >= 18 else 0)
print("\nAfter Feature Creation (BMI, Is_Adult):\n", data)

data['Log_Income'] = np.log(data['Income'])
print("\nAfter Log Transformation on Income:\n", data[['Income', 'Log_Income']])

scaler = MinMaxScaler()
data[['Height_scaled', 'Weight_scaled', 'Age_scaled']] = scaler.fit_transform(data[['Height', 'Weight', 'Age']])
print("\nAfter Min-Max Scaling:\n", data[['Height_scaled', 'Weight_scaled', 'Age_scaled']])

le = LabelEncoder()
data['Gender_encoded'] = le.fit_transform(data['Gender'])
print("\nAfter Label Encoding Gender:\n", data[['Gender', 'Gender_encoded']])

# Define X and y (Target: Gender_encoded)
X = data[['Height', 'Weight', 'Age', 'BMI', 'Income']]
y = data['Gender_encoded']

selector = SelectKBest(score_func=f_classif, k=3)
X_selected = selector.fit_transform(X, y)
selected_cols = X.columns[selector.get_support()]
print("\nSelected Features (Top 3 by ANOVA F-test):\n", selected_cols)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(data[['Height', 'Weight', 'Age']])
pca_df = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
print("\nPCA Output (2 Principal Components):\n", pca_df)