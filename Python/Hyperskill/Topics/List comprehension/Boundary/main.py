numbers = [int(n) for n in input()]
print([x for x in numbers if x < 5], [x for x in numbers if x > 5], sep='\n')
