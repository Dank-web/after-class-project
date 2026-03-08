import math

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

# taking input from user
r = float(input("Enter the radius of the circle: "))

result = calculate_circumference(r)

print("The circumference of the circle is:", result)