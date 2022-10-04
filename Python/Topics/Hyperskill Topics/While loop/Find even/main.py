num = int(input())
while num > 0:
    for i in range(1, num):
        if i % 2 == 0:
            print(i)
            num -= 1
        num -= 1
