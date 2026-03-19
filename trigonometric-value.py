import math

# take input from user
angle = float(input("Enter angle in degrees: "))

# convert degrees to radians
radians = math.radians(angle)

# calculate values
sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

# print results
print("sin(", angle, ") =", sin_value)
print("cos(", angle, ") =", cos_value)
print("tan(", angle, ") =", tan_value)