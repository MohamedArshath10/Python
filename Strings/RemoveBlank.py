def remove_blank(word):
    for char in word:
        if (char == ' '):
            word = word.replace(char, '')
    print(word)
remove_blank("hello world")