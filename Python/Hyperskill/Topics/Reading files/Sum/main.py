with open('sums.txt') as sample:
    for line in sample:
        print(sum([int(char) for char in line.split()]))
    sample.close()
