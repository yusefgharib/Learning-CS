coins = int(input())
prices = {'chicken': 23, 'goat': 678, 'pig': 1296, 'cow': 3848, 'sheep': 6769}
afford = None
animal = None
for key in prices:
    if coins >= prices[key]:
        afford = prices[key]
        animal = key
    else:
        break

if afford is None and animal is None:
    print("None")
else: 
    count = coins // afford
    if count == 1 or animal == 'sheep':
        print(f'{count} {animal}')
    else: 
        print(f'{count} {animal}s')
