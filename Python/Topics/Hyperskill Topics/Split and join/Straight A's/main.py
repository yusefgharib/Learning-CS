grades = input().split()
count = 0
for grade in grades:
    if grade == 'A':
        count += 1
print(round(count / len(grades), 2))
