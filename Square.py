import turtle    # importing library

screen = turtle.Screen()
screen.bgcolor("orange")
screen.setup(300, 400)

polygon = turtle.Turtle()  # defined variable

num_sides = 4
side_length = 70
angle = 360 / num_sides   # correct angle for square

# iterate loop for total number of sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()
