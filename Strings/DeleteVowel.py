def DeleteVowel(word):
    new_word = ""
    for char in word:
        if char not in 'aeiouAEIOU':
            new_word = new_word + char
    print(new_word)
word = input()
DeleteVowel(word)