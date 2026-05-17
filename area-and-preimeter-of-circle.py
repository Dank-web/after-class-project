# Python program to create a Circle class

import math

class Circle:
    # Constructor
    def __init__(self, radius):
        self.radius = radius

    # Method to compute area
    def compute_area(self):
        return math.pi * self.radius * self.radius

    # Method to compute perimeter (circumference)
    def compute_perimeter(self):
        return 2 * math.pi * self.radius


# Creating an object
c1 = Circle(7)

# Displaying results
print("Radius:", c1.radius)
print("Area of Circle:", c1.compute_area())
print("Perimeter of Circle:", c1.compute_perimeter())