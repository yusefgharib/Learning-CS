h = int(input())
for i in range(1, h + 1):
    print(' ' * (h - i) + '#'.join(i * '#'))
