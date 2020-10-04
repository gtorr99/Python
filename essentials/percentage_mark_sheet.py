total_marks = 300
marks = 0
f = open('C:/Users/GTorr/Documents/VSCode/Workspace/Python/essentials/marksheet.txt')

for line in f:
    ls = list(line.split())
    marks += int(ls[1]) + int(ls[2]) + int(ls[3])

f.close()
percentage = (marks / total_marks) * 100
print(percentage)
if percentage >= 40:
    print("Person has passed the exam")
else:
    print("Person hasn't passed the exam")

print(marks)
print(ls)