s = c = 0
while True:
    num = input()
    if num == '.':
        break
    s += int(num)
    c += 1
print(s / c)
