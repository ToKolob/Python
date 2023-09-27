square_lenght = float( input("What is the length of a side of the square? "))
square_area = square_lenght * square_lenght 
print (f"The area of the square is: {square_area:.2f}\n")

rectangle_lenght = float(input("What is the length of the rectangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))
rectangle_area = rectangle_lenght * rectangle_width 
print (f"The area of the rectangle is: {rectangle_area:.2f}\n")

circle_radius = float(input("What is the radius of the circle? "))
circle_area = (circle_radius ** 2) * 3.14
print (f"The area of the circle is: {circle_area:.2f}\n")

#I try to import math to do so I saw in the streched solution
import math
circle_area = (circle_radius ** 2)  * math.pi
print (f"Or, more precisely, using a hole constant of pi, the area of the circle is: {circle_area:.6f}")
