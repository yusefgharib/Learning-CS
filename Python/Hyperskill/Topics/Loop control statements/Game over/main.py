scores = input().split()
c = s = 0
for char in scores:
    s += 1
    if char == 'I':
        c += 1
    if c == 3:
        print("Game over")
        print(s - c)
        break
else:
    print("You won")
    print(s - c)
