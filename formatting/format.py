from datetime import datetime

############################
# Big numbers
############################

num: int = 1_000_000_000 # use underscores to read the number better.  They are ignored
print(num)
# output a string, which is a number with commas as thousands separators
print(f'{num:,}')
floater: float = 1234.567
print(f'{floater:,.2f}')


############################
# Calculations
############################

a: int = 5
b: int = 10
my_var: str = 'Hmmmm'
# Instead of:
print(f'a + b = {a + b}')
# can write:
print(f'{a + b = }')
# which is awesome for debugging as below:
print(f'{my_var = }')

############################
# Spacing and alignment
############################


my_str: str = 'var'
# output a string, which is right aligned and takes up 20 characters including filler spaces
print(f'{my_str:>20}')
# < for left align which is default.  ^ for centre.
# Can add a fill element as follows:
print(f'{my_str:_^20}')

############################
# Date time
############################

now: datetime = datetime.now()
print(f'{now:%d/%m/%y (%H:%M:%S)}')
# local version of datetime
print(f'{now:%c}')
# AM/PM format
print(f'{now:%I%p}')