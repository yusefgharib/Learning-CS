name = input()
def normalize(person):
    symbols = {'é': 'e', 'ë': 'e', 'á': 'a', 'å': 'a', 'œ': 'oe', 'æ': 'ae'}
    for key in symbols:
        person = person.replace(key, symbols[key])
    return person
print(normalize(name))
