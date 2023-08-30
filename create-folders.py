import os

folder_root = 'C:\\Users\\brian.blackie\\OneDrive - Trinity Schools\\Classes\\11DGT\\Assessment\\AS91886 1.10 HCI\\Student work\\'
folder_root = 'D:\\src\\11DGT\\'

# C:\Users\brian.blackie\OneDrive - Trinity Schools\Classes\12DGT\Assessments\2.2 Design\Student work

with open('names-Y11.txt') as x:
    for line in x:
        line = line.strip()
        os.mkdir(folder_root + str(line))


