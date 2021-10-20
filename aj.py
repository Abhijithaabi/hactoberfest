stud = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    stud.append([name,score])
    scores.append(score)
stud = sorted(stud)
mi = min(scores)
while min(scores) == mi :
    scores.remove(min(scores))
for marks in stud :
    for nam in marks :
        if nam == min(scores):
            print(marks[0])
