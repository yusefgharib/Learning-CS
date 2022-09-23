a, b, h = [int(input()) for _ in range(3)]
print('Deficiency' if h < a else 'Excess' if h > b else 'Normal')
