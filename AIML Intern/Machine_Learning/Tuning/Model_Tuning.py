from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
import numpy as np

# 1. Sample Data
X = np.random.rand(1000, 10)
y = np.random.randint(0, 2, size=(1000,))

# 2. Model
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 3. Early Stopping
early_stop = EarlyStopping(
    monitor='val_loss',      # watch validation loss
    patience=3,              # stop after 3 epochs without improvement
    restore_best_weights=True
)

# 4. Train
history = model.fit(
    X, y,
    validation_split=0.2,
    epochs=50,
    callbacks=[early_stop],
    verbose=1
)