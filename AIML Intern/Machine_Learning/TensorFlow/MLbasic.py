# Import Libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Sample Input and Output (XOR Problem)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([[0],
              [1],
              [1],
              [0]])

# Step 1: Build ANN Model
model = Sequential()

# Input Layer + Hidden Layer
model.add(Dense(4, input_dim=2, activation='relu'))

# Output Layer
model.add(Dense(1, activation='sigmoid'))

# Step 2: Compile the Model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Step 3: Train the Model
model.fit(X, y, epochs=100, verbose=0)  # Set verbose=1 if you want to see training logs

# Step 4: Evaluate the Model
loss, accuracy = model.evaluate(X, y)
print(f"Model Loss: {loss:.4f}")
print(f"Model Accuracy: {accuracy:.4f}")

# Step 5: Make Predictions
predictions = model.predict(X)
print("Predictions:")
print(np.round(predictions))  # Round output to 0 or 1