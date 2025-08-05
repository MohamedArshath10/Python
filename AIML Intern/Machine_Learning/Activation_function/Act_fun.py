import numpy as np
import matplotlib.pyplot as plt

# Define activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

# Generate 100 evenly spaced values from -10 to 10
x = np.linspace(-10, 10, 100)

# Plot the activation functions
plt.plot(x, sigmoid(x), label='Sigmoid')
plt.plot(x, np.tanh(x), label='Tanh')
plt.plot(x, relu(x), label='ReLU')

# Add legend and title
plt.legend()
plt.title("Activation Functions")

# Add grid
plt.grid()

# Display the plot
plt.show()