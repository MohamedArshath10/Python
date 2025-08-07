import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=UserWarning)
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Sample data
data = {
    'text': ["I love this movie", "This film is terrible", "Fantastic experience", "Not good", "Absolutely amazing"],
    'label': [1, 0, 1, 0, 1]  # 1 = Positive, 0 = Negative
}
df = pd.DataFrame(data)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print(classification_report(y_test, y_pred))