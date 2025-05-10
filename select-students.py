import os
import random

intro = '''
#####################################
###       STUDENT RANDOMISER      ### 
#####################################
Matches the logic of most students!
'''
list = 'names-Y13.txt'

students = []
selected = []

def print_names(student_list):
    for student in student_list:
        print(student)

with open(f'data/classes/{list}') as x:
    for line in x:
        students.append(line.replace('\n',''))
        


print(intro)
print("\n### ORDERED BY LASTNAME...\n")        
print_names(students)


for i in range(len(students)):
    num_students_left = len(students)
    rand_idx = random.randint(0, num_students_left-1)
    selected.append(students[rand_idx])
    students.pop(rand_idx)
    
    
print("\n\n### COMPLETELY RANDOMISED...\n")        
print_names(selected)
print('\n')
