import random
sentence = input().split()
random.seed(43)
random.shuffle(sentence)
print(' '.join(sentence))
