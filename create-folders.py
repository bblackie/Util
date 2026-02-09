import os


list = 'initials-Y12.txt'
folder_root = 'C:\\Repos\\12DGT\\91893-web\\'

list2 = 'subjects.txt'
folder_root2 = 'C:\\Users\\brian\\OneDrive - Trinity Schools\\NCEA\\L3\\achievements\\AS91908 (3.9) - CS Area\\Past exams\\by topic\\'

#folder_root = 'C:\\Users\\brian.blackie\\OneDrive - Trinity Schools\\NCEA\\Exams - DCATs\\DCATs\\L3\\91909\\Student submissions\\'
#folder_root = 'D:\\src\\11DGT\\'

# C:\Users\brian.blackie\OneDrive - Trinity Schools\Classes\12DGT\Assessments\2.2 Design\Student work




#with open(f'data/classes/{list}') as x:
with open(f'data/categories/{list2}') as x:
    for line in x:
        line = line.strip() 
        if not os.path.exists(folder_root2 + str(line)):
            os.mkdir(folder_root2 + str(line))


print('Mission complete.')