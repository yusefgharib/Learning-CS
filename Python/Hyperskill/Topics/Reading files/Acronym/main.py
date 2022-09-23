with open('test.txt') as test:
    for line in test:
        print(line[0])
    test.close()
