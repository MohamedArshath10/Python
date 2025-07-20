def Pangram(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word = word.lower().replace(" ", "")
    for letter in alphabet:
        if letter not in word:
            print("false")
            return
    print("true")
Pangram("the quick brown fox jumps over the lazy dog")