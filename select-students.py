import os
import random

list = 'names-Y11.txt'

students = []
selected = []

with open(f'data/classes/{list}') as x:
    for line in x:
        students.append(line.replace('\n',''))
        
        
print(students)


for i in range(len(students)):
    rand_idx = random.randint(0, len(students))
    selected.append(students[rand_idx])
    students.pop(rand_idx)
    print("\nStudents: ", students)
    print("\nSelected:", selected)
    print("#############")