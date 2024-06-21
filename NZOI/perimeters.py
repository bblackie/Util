
'''
Alison is in year 7 and she love Maths, in particular Measurement. She figures that to work out the perimeter of a rectangle she doesn't need the lengths of all sides to be given to her. If the rectangle is drawn on a plane (fancy word alert: Cartesian plane) and the sides of the rectangle are parallel to the x and y axes, then she can figure the perimeter if she is given the bottom left vertex (unfancy word: corner) coordinates and the top right vertex coordinates.

Input
The first line of input contains 2 integers, A and B, the x and y coordinates of the bottom left hand vertex.

The second line of input contains 2 integers, C and D, the x and y coordinates of the top right hand vertex.

Output
Print a single integer - the distance on the Cartesian plane that is the perimeter of the rectangle.

Subtasks
For all test cases, A<C and B<D. The following subtasks are available:

Subtask 1 (50%): A,B,C,D>0
Subtask 2 (50%): −1000≤A,B,C,D≤1000

'''


bottom_left_coord = []
top_right_coord = []

# input contains 2 integers, A and B, the x and y coordinates, which are separted by a space
# e.g. 2 2
bottom_left_coord_text = input()
bottom_left_coord = bottom_left_coord_text.split()


# input contains 2 integers, C and D, the x and y coordinates, 
top_right_coord_text = input()
top_right_coord = top_right_coord_text.split()

horizontal_distance = int(top_right_coord[0]) - int(bottom_left_coord[0])
vertical_distance = int(top_right_coord[1]) - int(bottom_left_coord[1])

perimeter = 2 * horizontal_distance + 2 * vertical_distance

print(perimeter)

