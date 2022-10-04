score, poss = int(input()), int(input())
grade = {"A": 90, "B": 80, "C": 70, "D": 60, "F": 0}
for key in grade:
    if grade[key] <= (score / poss * 100):
        print(key)
        break
