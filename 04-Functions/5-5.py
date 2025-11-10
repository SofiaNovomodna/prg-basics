###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle
import random

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)   

## Draw figures
figures.draw_rectangle(pen, 30, 46)
pen.penup()
pen.goto(random.randrange(-400, 400), random.randrange(-400, 400))
pen.pendown()

figures.draw_square(pen, 50)
pen.penup()
pen.goto(random.randrange(-400, 400), random.randrange(-400, 400))
pen.pendown()

figures.draw_triangle(pen, 68)
pen.penup()
pen.goto(random.randrange(-400, 400), random.randrange(-400, 400))
pen.pendown()

figures.draw_rectangle(pen, 30, 46)
pen.penup()
pen.goto(random.randrange(-400, 400), random.randrange(-400, 400))
pen.pendown()

figures.draw_square(pen, 50)
pen.penup()
pen.goto(random.randrange(-400, 400), random.randrange(-400, 400))
pen.pendown()

figures.draw_triangle(pen, 68)
pen.penup()
pen.goto(random.randrange(-400, 400), random.randrange(-400, 400))
pen.pendown()

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()