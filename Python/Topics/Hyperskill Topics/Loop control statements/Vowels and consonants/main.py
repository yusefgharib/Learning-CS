vowel, word = ['a', 'e', 'i', 'o', 'u'], input()
for character in word:
    if not character.isalpha():
        break
    elif character in vowel:
        print("vowel")
    else:
        print("consonant")
