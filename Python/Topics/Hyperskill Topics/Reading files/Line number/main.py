count = 0
with open('sample.txt', 'rt') as f:
    for _ in f:
        count += 1
    f.close()
print(count)
