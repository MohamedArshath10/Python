import seaborn as sns
import matplotlib.pyplot as plt
data = [10, 20, 20, 30, 30, 30, 40, 40, 40, 50]
sns.histplot(data, kde=True)
plt.title('Histogram')
plt.show()