import os
import random

list = 'names-Y12.txt'

students = []
selected = []

def print_pairs(student_list1, student_list2):
    for n in range(len(student_list1)):
        print(f"{student_list1[n]} :: {student_list2[n]}")

with open(f'data/classes/{list}') as x:
    for line in x:
        students.append(line.replace('\n',''))
        



for i in range(len(students)):
    num_students_left = len(students)
    rand_idx = 0
    while True:
        rand_idx = random.randint(0, num_students_left-1)
        #print(rand_idx, len(students), len(selected))
        if rand_idx < len(selected):
            break
        elif students[rand_idx] != selected[rand_idx]:
            break
    selected.append(students[rand_idx])
    students.pop(rand_idx)
    
print("\n\n### PAIRS...\n")        
print_pairs(students, selected)
print('\n')