students={}
for x in range(3):
    student=input(f"Enter your name {x+1}:")  
    marks=int(input(f"Enter you marks {x+1}:"))
    students[student]=marks
print(students)
