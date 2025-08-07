from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np

# Sample Data
texts = ["I love this movie", "Worst experience", "Best film ever", "Terrible storyline", "So good"]
labels = [1, 0, 1, 0, 1]

# Tokenization
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded = pad_sequences(sequences, maxlen=5)

# Model
model = Sequential([
    Embedding(input_dim=1000, output_dim=16, input_length=5),
    LSTM(32),
    Dense(1, activation='sigmoid')
])

# Compile
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train
model.fit(np.array(padded), np.array(labels), epochs=10)