from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
import matplotlib.pyplot as plt

# Generate sample data
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)

# Fit KMeans model
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(X)

# Labels and cluster centers
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Evaluation
sil_score = silhouette_score(X, labels)
db_score = davies_bouldin_score(X, labels)

print("Silhouette Score:", sil_score)
print("Davies-Bouldin Index:", db_score)

# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, label='Centroids')
plt.title("Cluster Analysis Result")
plt.legend()
plt.show()