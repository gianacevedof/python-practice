# calculating the circumference of a circle
import math

print("First, let's calculate the circumference of a circle.")
radius = float(input("To calculate the circumference of your circle, please enter its radius: "))
circumference = 2 * math.pi * radius
print(f"The circumference of your circle is {circumference:.2f}")

print("\nNow, let's get its area.")
radius2 = float(input("Enter the radius of your circle: "))
area = math.pi * pow(radius2, 2)
print(f"The area of your circle is {area:.2f} cm^2.")

print("\nLast, let's get the hypoenuse of a right triangle.")
a = float(input("To get the hypotenuse of your triangle, please enter the lenght of its size 'a': "))
b = float(input("Now, enter the lenght of its size 'b': "))
hypo = math.sqrt(a**2 + b**2)
print(f"The hypotenuse of your triangle is {hypo:.1f}.")