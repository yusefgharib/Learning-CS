sentence = input().split()
repeat = []
for word in sentence:
    if word.endswith('s'):
        repeat.append(word)
print(*repeat, sep='_')
