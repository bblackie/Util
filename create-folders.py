import os


def create_folders_by_class(list, folder_root):
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

# create folders by class
list = 'initials-Y11.txt'
folder_root = 'C:\\repos\\11DGT\\godot-internal\\'
create_folders_by_class(list, folder_root)

# create folders by subject
# list2 = 'subjects.txt'
# folder_root2 = 'C:\\Users\\brian\\OneDrive - Trinity Schools\\NCEA\\L3\\achievements\\AS91908 (3.9) - CS Area\\Past exams\\by topic\\'
# create_folders_by_subject(list2, folder_root2)


print('Mission complete.')