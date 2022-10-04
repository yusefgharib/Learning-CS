dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
words = input().split()
incorrect = ""
for word in words:
    if word not in dictionary:
        incorrect = word
        print(incorrect)
if incorrect == '':
    print("OK")
