import os

# Year groups
list = 'initials-Y13.txt'
folder_root = 'C:\\Users\\brian\\OneDrive - Trinity Schools\\Classes\\13DGT\\Assessments\\AS91901(3.2) Design\\Student work\\'


# Subject groups
list2 = 'subjects.txt'
folder_root2 = 'C:\\Users\\brian\\OneDrive - Trinity Schools\\NCEA\\L3\\achievements\\AS91908 (3.9) - CS Area\\Past exams\\by topic\\'

#folder_root = 'C:\\Users\\brian.blackie\\OneDrive - Trinity Schools\\NCEA\\Exams - DCATs\\DCATs\\L3\\91909\\Student submissions\\'
#folder_root = 'D:\\src\\11DGT\\'

# C:\Users\brian.blackie\OneDrive - Trinity Schools\Classes\12DGT\Assessments\2.2 Design\Student work


def create_folders_by_year(list, folder_root):
    with open(f'data/classes/{list}') as x:

        for line in x:
            line = line.strip() 
            if not os.path.exists(folder_root + str(line)):
                os.mkdir(folder_root + str(line))

def create_folders_by_subject(list, folder_root):
    
    with open(f'data/categories/{list}') as x:
        for line in x:
            line = line.strip() 
            if not os.path.exists(folder_root + str(line)):
                os.mkdir(folder_root + str(line))



create_folders_by_year(list, folder_root)
#create_folders_by_subject(list2, folder_root2)

print('Mission complete.')