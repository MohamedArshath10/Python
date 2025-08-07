from sklearn.feature_extraction.text import TfidfVectorizer

# Sample corpus
docs = [
    "Natural Language Processing is amazing",
    "Language models learn from data",
    "Processing text data is a major task in NLP"
]

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform
tfidf_matrix = vectorizer.fit_transform(docs)

# Show feature names
print("Feature Names:", vectorizer.get_feature_names_out())

# Show TF-IDF matrix
print("\nTF-IDF Matrix:\n", tfidf_matrix.toarray())