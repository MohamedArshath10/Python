def Reverse(word):
    reversString = ""
    for char in word:
        reversString = char + reversString
    return reversString

print(Reverse("hello"))