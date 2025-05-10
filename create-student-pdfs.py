import os
from reportlab.pdfgen import canvas
import shutil


def create_pdf(filename):
    c = canvas.Canvas(f"{filename}")
    c.drawString(100, 750, "Hello, I am a PDF document created with Python!")
    c.save()

list = 'names-nsn-Y12.txt'
folder_root = 'C:\\Users\\brian.blackie\\OneDrive - Trinity Schools\\Classes\\12DGT\\Assessments\\AS91899(2.10) Reflective Summary\\Student work\\'
#folder_root2 = 'C:\\Users\\brian.blackie\\OneDrive - Trinity Schools\\Classes\\13DGT\\Assessments\\3.7 Computer Program\\Student work\\'


#folder_root = 'C:\\Users\\brian.blackie\\OneDrive - Trinity Schools\\NCEA\\Exams - DCATs\\DCATs\\L3\\91909\\Student submissions\\'
#folder_root = 'D:\\src\\11DGT\\'

# C:\Users\brian.blackie\OneDrive - Trinity Schools\Classes\12DGT\Assessments\2.2 Design\Student work





with open(f'data/classes/{list}') as x:
    for line in x:
        stud_dees = line.strip().split(",")
        
        filename = f"{stud_dees[1]}.pdf"
        create_pdf(filename)
        foldername = folder_root + str(stud_dees[0])
        
        
        if not os.path.exists(foldername):
            os.mkdir(foldername)
            

        shutil.move(f".\\{filename}", f"{foldername}\\{filename}")

print('Mission complete.')