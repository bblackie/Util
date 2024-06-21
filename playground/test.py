import random

hungry = True
while hungry:
    print("Eating, eating")
    if random.randrange(1, 10) > 5:
        hungry = False
        print("I'm full now")       
        
print("Nice meal")

