import re
import string
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords

text = "Hello!!! This is an example text, with numbers like 123 and symbols *&^%$."

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))



# Remove numbers
text = re.sub(r'\d+', '', text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
words = text.split()
cleaned_words = [word for word in words if word not in stop_words]

cleaned_text = ' '.join(cleaned_words)
print("Cleaned Text:", cleaned_text)