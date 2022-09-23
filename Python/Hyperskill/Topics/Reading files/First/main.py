with open('test_file.txt', 'rt', encoding='utf-16') as test:
    print(test.readline())
    test.close()
