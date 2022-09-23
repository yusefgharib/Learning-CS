word = input()
neg = -1
for i in range(len(word)):
    if word[i] != word[neg]:
        print("Not palindrome")
        break
    elif word[i] == word[neg]:
        neg -= 1
        continue
else:
    print("Palindrome")    
# or 
# word = input()
# print("Palindrome" if word == word[::-1] else "Not palindrome")
