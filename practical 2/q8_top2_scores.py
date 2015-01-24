students = int(input("Enter number of students: "))
names = []
score = []
while students != 0:
    names.append(input("Enter name: "))
    score.append(int(input("Enter score: ")))
    students -= 1
highest = max(score)
print("Student with highest score is:", names[score.index(highest)], "with a score of:", highest)
names.pop(score.index(highest))
score.pop(score.index(highest))
highest2 = max(score)
print("Student with second highest score is:", names[score.index(highest2)],
      "with a score of:", highest2)
