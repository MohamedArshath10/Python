def isAnagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False


word1 = "a gentleman"
word2 = "elegant man"
print(isAnagram(word1, word2))