with open('animals.txt') as names:
    text = names.read()
    names.close()
with open('animals_new.txt', 'w') as new_names:
    new_names.write(text.replace('\n', ' ').strip())
    new_names.close()
