def RemoveVowels(word):
    vowels = "aeiou"
    word = word.lower()
    removedWord = ""
    for char in word:
        if char not in vowels:
            removedWord += char
    return removedWord

word = "Aafiya"
print(RemoveVowels(word))
