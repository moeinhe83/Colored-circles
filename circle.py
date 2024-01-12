# Library
import turtle

# Turtle For Value
turtle.bgcolor('black')
turtle.pensize(5)
turtle.speed(0.5)
color = ['red', 'blue', 'yellow', 'cyan']

# Draw
for i in range(9):
    for a in color:
        turtle.color(a)
        turtle.circle(90)
        turtle.right(10)
turtle.mainloop()


# Finish
# Create By Moein Heshmati