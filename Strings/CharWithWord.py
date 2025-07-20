def NoOfWords(str):
    wordCount = 0
    newstr = str.split()
    for char in newstr:
        wordCount += 1
    print("The number of words: ", wordCount)

def NoOfChar(str):
    strlen = len(str)
    print("The number of characters: ",strlen)

str = "hello how are you!"
NoOfWords(str)
NoOfChar(str)