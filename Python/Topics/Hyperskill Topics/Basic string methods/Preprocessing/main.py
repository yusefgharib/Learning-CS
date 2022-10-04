sent = input().lower()
marks = ',.!?'
for char in marks:
    sent = sent.replace(char, '')
print(sent)
