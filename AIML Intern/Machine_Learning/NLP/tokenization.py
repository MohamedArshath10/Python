from nltk.tokenize import word_tokenize, sent_tokenize
import  nltk
# nltk.download('punkt')

text = "Natural Language Processing is fun. It helps computers understand text!"

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentences:", sentences)

# Word Tokenization
words = word_tokenize(text)
print("Words:", words)