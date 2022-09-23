from collections import defaultdict
max_students = int(input())
math, physics, bio, chem, engineering, students = [], [], [], [], [], []
with open('applicant_list_7.txt', 'r') as f:
    for line in f.readlines():
        student = line.split()
        name = student[0] + ' ' + student[1]
        scores = [0, 0]
        if len(student) == 10:
            for i in range(2):
                scores[i] = max(int(student[4]), int(student[6])) if student[i + 8] == "Mathematics" \
                    else max((int(student[2]) + int(student[4])) / 2, int(student[6])) if student[i + 8] == 'Physics' \
                    else max((int(student[3]) + int(student[2])) / 2, int(student[6])) if student[i + 8] == 'Biotech' \
                    else max(int(student[3]), int(student[6])) if student[i + 8] == 'Chemistry' \
                    else max((int(student[5]) + int(student[4])) / 2, int(student[6]))
            students.append([name, scores[0], scores[1], student[8], student[9]])
            if student[7] == 'Mathematics':
                math.append([name, max(int(student[4]), int(student[6]))])
            elif student[7] == 'Physics':
                physics.append([name, max((int(student[2]) + int(student[4])) / 2, int(student[6]))])
            elif student[7] == 'Biotech':
                bio.append([name, max((int(student[3]) + int(student[2])) / 2, int(student[6]))])
            elif student[7] == 'Chemistry':
                chem.append([name, max(int(student[3]), int(student[6]))])
            elif student[7] == 'Engineering':
                engineering.append([name, max((int(student[5]) + int(student[4])) / 2, int(student[6]))])
applications = {"Biotech": bio, "Chemistry": chem, "Engineering": engineering, "Mathematics": math, "Physics": physics}
for key in applications:
    applications[key].sort(key=lambda x: (-x[1], x[0]))
accepted_students = defaultdict(list)
for subject in applications:
    for i in range(max_students):
        if i >= len(applications[subject]):
            break
        accepted_students[subject].append([applications[subject][i][0], applications[subject][i][1]])
        for student in students:
            if student[0] == applications[subject][i][0]:
                students.remove(student)
for j in range(2):
    students.sort(key=lambda x: (-x[1 + j], x[0]))
    for key in accepted_students:
        if len(accepted_students[key]) < max_students:
            for i, name in enumerate(students):
                if len(accepted_students[key]) == max_students:
                    break
                if name[3 + j] == key:
                    accepted_students[key].append([name[0], name[1 + j]])
                    students[i] = ["0", 0, 0, "0", "0"]
for key in dict(accepted_students):
    accepted_students[key] = sorted(accepted_students[key], key=lambda x: (-x[1], x[0]))
for subject in accepted_students:
    with open(f"{subject.lower()}.txt", "w") as f:
        content = ''
        for student in accepted_students[subject]:
            content += f"{student[0]} {student[1]}\n"
        f.write(content)
