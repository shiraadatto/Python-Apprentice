"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle  
import random                         # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina
tina.speed(10)
# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()
turtle.bgcolor("black")

def drawStar():
    x = random.randint(-300, 300)
    y = random.randint(0, 300)
    tina.goto(x, y)
    tina.pencolor("white")
    tina.fillcolor("white")
    tina.pendown()
    tina.begin_fill()
    tina.circle(2)
    tina.end_fill()
    tina.penup()

for i in range(30):
    drawStar()


colors = ["red", "blue", "green", "yellow", "purple", "orange"]

def drawBuilding():
    tina.setheading(0)
    tina.color(colors[random.randint(0,5)])
    tina.pendown()
    tina.begin_fill()
    tina.forward(100)
    tina.left(90)
    tina.forward(400)
    tina.left(90)
    tina.forward(100)
    tina.left(90)
    tina.forward(400)
    tina.end_fill()
    tina.penup()
    tina.setheading(0)
    tina.forward(25)
    tina.left(90)
    tina.forward(200)
    tina.pencolor("yellow")
    tina.pendown()
    tina.left(90)
    tina.forward(30)
    tina.left(90)
    tina.forward(30)
    tina.left(90)
    tina.forward(30)
    tina.penup()

tina.goto(-300,-300)

for i in range(1):
    drawBuilding()
    tina.forward(105)

... # Your code here

turtle.exitonclick()                    # Close the window when we click on it
