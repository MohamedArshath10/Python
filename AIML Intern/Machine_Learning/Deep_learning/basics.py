import numpy as np

def step_function(x):
    return 1 if x > 0 else 0

def perceptron(x1, x2):
    w1, w2 = 1, 1
    bias = -1.5
    x = x1 * w1 + x2 * w2 + bias
    return step_function(x)

print(perceptron(0, 0))  # Output: 0
print(perceptron(0, 1))  # Output: 0
print(perceptron(1, 0))  # Output: 0
print(perceptron(1, 1))  # Output: 1