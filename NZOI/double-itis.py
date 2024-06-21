# A program to parse Andrew's double-itis
# It will calculate his real age

'''
Andrew has double-itis. This means whenever you ask him any question, he answers with the correct answer, doubled.

Because we're trying to go to a theme park this year, we want to know how old Andrew really is. Your job, given the age Andrew has 
told you he is, and the minimum age for the theme park, is to tell us whether or not we can take Andrew to the theme park.

You should always round down the results of any division, which means that if you are given 9, and it becomes 4.5, you should round 
down the result to 4, before comparing it to the minimum age the theme park requires.

Input
You'll be given two integers N and M, separated by a newline (0≤N,M≤50). The first integer is the age that Andrew says he is, and 
the second integer is the minimum age for the theme park we want to visit.

Output
You should output No, if Andrew’s real age is LESS THAN the minimum age of the theme park, and Yes in every other case.
'''

# Inputs are two integers N and M, separated by a newline (0≤N,M≤50).
purported_age = int(input())
ride_age_min = int(input())

if purported_age < 0 or ride_age_min > 50:
    print("An inputted value is invalid")

else:
    
    actual_age = purported_age // 2
    
    if actual_age < ride_age_min:
        print("No")
    else:
        print("Yes")
