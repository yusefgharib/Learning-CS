text = input().split()
for word in text:
    if word.lower().startswith(('www.', 'http')):
        print(word)
