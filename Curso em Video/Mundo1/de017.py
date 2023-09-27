import math
cateto1 = float(input("qual o valor do primeiro cateto? "))
cateto2 = float(input("qual o valor do segundo cateto? "))
hipotenusa = math.hypot(cateto1,cateto2)
print (hipotenusa)