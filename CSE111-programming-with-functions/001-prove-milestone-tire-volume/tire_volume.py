import math as mt


print(1+3*7%4+2)

width = float(input('\nEnter the width of the tire in mm  '))
aspect_radio = float(input('Enter the aspect ratio of the tire  '))
diameter = float(input('Enter the diameter of the wheel in inches  '))
pi = mt.pi

volume = (pi*(width**2)*aspect_radio*(width*aspect_radio+2540*diameter))/(10**10)

print (f'\nThe approximate volume is {volume:.2f} liters\n')

