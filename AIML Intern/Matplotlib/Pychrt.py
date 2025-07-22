import matplotlib.pyplot as plt

# Data
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [25, 30, 20, 25]
colors = ['red', 'yellow', 'purple', 'brown']
explode = (0, 0, 0, 0)

# Create pie chart
plt.pie(sizes, labels=labels, colors=colors, explode=explode, startangle=140)
plt.axis('equal')

# Show plot
plt.title("pala kooda")
plt.show()
