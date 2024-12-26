import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Star Animation")

# Create a turtle for drawing stars
star_turtle = turtle.Turtle()
star_turtle.speed(0)  # Set the drawing speed to the maximum

# Function to draw a star
def draw_star(size):
    star_turtle.color("white")
    star_turtle.begin_fill()
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)
    star_turtle.end_fill()

# Function to move the turtle to a random position
def move_to_random_position():
    x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
    y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.pendown()

# Main animation loop
for _ in range(50):  # You can adjust the number of stars as needed
    star_size = random.randint(10, 30)
    move_to_random_position()
    draw_star(star_size)

# Hide the turtle
star_turtle.hideturtle()

# Close the window on click
screen.exitonclick()
