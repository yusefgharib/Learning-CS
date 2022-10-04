wins = [input().split() for _ in range(int(input()))]
names = [wins[i][0] for i in range(len(wins)) if wins[i][1] == 'win']
print(names)
print(len(names))
