added, counter = 0, 0
for i in range(int(input()), int(input()) + 1):
    if i % 3 == 0:
        added += i
        counter += 1
print(added / counter)
