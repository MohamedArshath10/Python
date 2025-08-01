from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
inertia = []
k = range(1, 11)
iris = load_iris()
X = iris.data
for i in k:
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

# plot elbow curve
plt.plot(k, inertia, 'bo-')
plt.xlabel('Number of cluster k')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()