from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Step 1: Load the Wine dataset
wine = load_wine()
X = wine.data        # Feature matrix (13 features)
y = wine.target      # Target vector (3 wine classes)
feature_names = wine.feature_names

print("Original shape:", X.shape)

# Step 2: Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Apply PCA to reduce to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Reduced shape:", X_pca.shape)

# Step 4: Plot PCA result
plt.figure(figsize=(8,6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='plasma', edgecolor='k', s=80)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Wine Dataset')
plt.grid(True)
legend1 = plt.legend(*scatter.legend_elements(), title="Classes")
plt.gca().add_artist(legend1)
plt.colorbar(label='Wine Class')
plt.show()

# Step 5: Show explained variance ratio
print("\nExplained Variance Ratio of Each Component:")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"PC{i+1}: {var:.4f}")

print(f"\nTotal Variance Captured by 2 components: {sum(pca.explained_variance_ratio_):.4f}")