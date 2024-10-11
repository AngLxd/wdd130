#my_num= 2/3
#print(f"My number is: {my_num:.3f}")

#import math
#my_num= 4
#squared = math.pow(my_num, 10);
#truncated = math.floor (my_num)

#print(f'my number is: {truncated}')

#import math
#a= 7
#b= 13
#c= math.sqrt(a** 2 + b ** 2)

#print(f'C is {c}')

#a= 7
#b= 13
#c= math.hypot(a, b)
#print(f'c is {c}')
#x = 2
#y = 3
#z = 4  

#w = x + y * z  

#print(w)
import math
print (f"Welcome to the velocity calculator. Please enter the following:\n")
m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
c = (1 / 2) * p * A * C
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))
print(f"The inner value of c is: {c} ")
print(f"The velocity after 10.0 seconds is: {v} m/s")