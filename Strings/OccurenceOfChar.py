def OccurenceOfChar(word):
    word = word.lower()
    for i in range(len(word)):
        count = 1
        for j in range(i):
            if word[i] == word[j]:
                count += 1
        print(word[i], count)
word = "Aafiya"
OccurenceOfChar(word)