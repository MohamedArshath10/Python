text = "hello"
vowel = ['a', 'e', 'i', 'o', 'u']
vowelCount = 0
consonantCount = 0
for char in text:
    if char in vowel:
        vowelCount += 1
    else:
        consonantCount += 1

print("The number of vowels are : ", vowelCount)
print("The number of consonants are : ", consonantCount)