import os

folder = 'H:\\Resources\\JHC - James Hargest College\\Y11-L1\\Programming\\Python_Skill Level_Beginner'
#folder2 = 'H:\Resources\JHC - James Hargest College\Y11-L1\Programming\Python_Skill Level_Beginner'
folder3 = 'H:\Resources\TAC - Te Awamutu College - TO EXPLORE'
items = os.listdir(folder3)
#items = os.listdir(folder)
for item in items:
    print(item)
        