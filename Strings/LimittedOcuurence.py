def limited_occurence(word):
    word = word.lower()
    new_word = ""
    for i in range(len(word)):
        count = 1
        for j in range(i):
            if word[i] == word[j]:
                count += 1
        if count < 3:
            new_word += word[i]
    print(new_word)
limited_occurence("arshathahh")