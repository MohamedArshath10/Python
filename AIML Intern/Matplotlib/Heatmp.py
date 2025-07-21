import seaborn as sns
import matplotlib.pyplot as plt
data = [[1,2], [3,4]]
sns.heatmap(data ,annot=True)
plt.title('Heatmap')
plt.show()