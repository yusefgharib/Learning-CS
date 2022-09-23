offset = int(input())
ref = 10.5
if ref + offset <= 0:
    print("Monday")
elif ref + offset >= 24:
    print("Wednesday")
elif 0 < ref + offset < 24:
    print("Tuesday")
