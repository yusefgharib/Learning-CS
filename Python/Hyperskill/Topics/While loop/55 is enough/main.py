counter, added, end = 0, 0, 55
num = int(input())
while num != end:
    counter += 1
    added += num
    num = int(input())
print(counter, added, round(added / counter), sep='\n')
