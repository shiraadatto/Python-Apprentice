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

for i in range(40):
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

tina.goto(-300,-300)

for i in range(6):
    drawBuilding()
    tina.forward(105)


def drawWindow(x,y):
    tina.penup()
    tina.goto(x,y)
    tina.color("white")
    tina.setheading(90)
    tina.pendown()
    tina.begin_fill()
    tina.forward(30)
    tina.right(90)
    tina.forward(30)
    tina.right(90)
    tina.forward(30)
    tina.right(90)
    tina.forward(30)
    tina.end_fill()
  
def drawWindows(x,y): 
    drawWindow(x,y)
    drawWindow(x+35,y)
    drawWindow(x, y-55)
    drawWindow(x+35, y-55)
    drawWindow(x, y-110)
    drawWindow(x+35, y-110)
    drawWindow(x, y-165)
    drawWindow(x+35, y-165)

drawWindows(-285,30)
drawWindows(-180, 30)
drawWindows(-75, 30)
drawWindows(30, 30)
drawWindows(135, 30)
drawWindows(240, 30)
... # Your code here

turtle.exitonclick()                    # Close the window when we click on it
