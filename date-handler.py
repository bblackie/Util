

'''
Takes the following date range
08/02/2023 to 21/02/2023
And reformats it to
20230208_TO_20230221

Process:
Python substsring - string[start:end:step]

'''
import sys
 

#novopay_date_range = '08/02/2023 to 21/02/2023'
novopay_date_range = sys.argv[1]

new_date_range = '{2}{1}{0}_TO_{5}{4}{3}'.format(novopay_date_range[0: 2], novopay_date_range[3: 5], novopay_date_range[6: 10]
                                                 , novopay_date_range[14: 16], novopay_date_range[17: 19], novopay_date_range[20: 24])

print(new_date_range)

'''
print(novopay_date_range[0: 1])
print(novopay_date_range[3: 5])
print(novopay_date_range[6: 11])

print(novopay_date_range[14: 16])
print(novopay_date_range[17: 19])
print(novopay_date_range[20: 27])
'''