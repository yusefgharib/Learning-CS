string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
counter = 0
for characters in string:
    if characters in vowels:
        counter += 1
print(counter)
