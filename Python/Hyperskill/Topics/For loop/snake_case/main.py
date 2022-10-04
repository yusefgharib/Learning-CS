name = input()
under = "_"
for i in range(len(name)):
    if name[i].isupper():
        name = name[:i] + name[i].lower() + name[i + 1:]
        name = name[:i] + under + name[i:]
print(name)
