def Case(word):
    fWord = word[0].upper()
    remWord = ""
    for i in range (1, len(word)):
        remWord += word[i].lower()
    print(fWord + remWord)

def Case1(word):
    fWord = word[0].lower()
    remWord = ""
    for i in range (1, len(word)):
        remWord += word[i].upper()
    print(fWord + remWord)

word = "hello"
Case(word)
Case1(word)

