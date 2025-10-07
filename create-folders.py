import os


list = 'dge-num-y12.txt'
folder_root = 'C:\\Users\\Brian.Blackie\\OneDrive - Trinity Schools\\Classes\\12DGT\\Assessments\\AS91898(2.9) Comp Sci - AI\\Student work\\'
folder_root2 = 'C:\\Users\\brian.blackie\\OneDrive - Trinity Schools\\Classes\\13DGT\\Assessments\\3.7 Computer Program\\Student work\\'


#folder_root = 'C:\\Users\\brian.blackie\\OneDrive - Trinity Schools\\NCEA\\Exams - DCATs\\DCATs\\L3\\91909\\Student submissions\\'
#folder_root = 'D:\\src\\11DGT\\'

# C:\Users\brian.blackie\OneDrive - Trinity Schools\Classes\12DGT\Assessments\2.2 Design\Student work





with open(f'data/classes/{list}') as x:
    for line in x:
        line = line.strip()
        if not os.path.exists(folder_root + str(line)):
            os.mkdir(folder_root + str(line))


print('Mission complete.')