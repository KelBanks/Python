from turtle import Turtle, Screen
import random

# Create object from Turtle library
craig_turtle = Turtle()
craig_turtle.shape("turtle")

# Number of sides for shape
num_sides = 5

# Array for returning a set of colors
color_arr = ["Red","Blue","Green","Orange", "Red"]

# Method to draw shape based on degree of angle
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        craig_turtle.forward(100)
        craig_turtle.right(angle)

# For loop that generates hex shape and random selection of color_arr 
for shape_side_n in range(3,11):
    craig_turtle.color(random.choice(color_arr))
    draw_shape(shape_side_n)

# Create a screen object
screen = Screen()
# Method to listen for click to exit screen
screen.exitonclick()

