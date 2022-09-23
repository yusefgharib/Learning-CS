ticket = input()
half_1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
half_2 = int(ticket[-1]) + int(ticket[-2]) + int(ticket[-3])
if half_1 == half_2:
    print("Lucky")
else:
    print("Ordinary")
