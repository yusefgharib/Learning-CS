import json, requests
currency = input().upper()
data = json.loads(requests.get(f'http://www.floatrates.com/daily/{currency}.json').text)
if currency == 'USD':
    cache = {'EUR': data['eur']['rate']}
elif currency == 'EUR':
    cache = {'USD': data['usd']['rate']}
else:
    cache = {'USD': data['usd']['rate'], 'EUR': data['eur']['rate']}
while True:
    convert = input().upper()
    if convert == '':
        break
    amount = int(input())
    print('Checking the cache...')
    if convert in cache:
        print(f'Oh! It is in the cache...\nYou received {cache[convert] * amount} {convert}.')
    else:
        cache.update({convert: data[convert.lower()]['rate']})
        print(f'Sorry, but it is not in the cache!\nYou received {cache[convert] * amount} {convert}.')
