"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error


# TODO)
#   1. Create a turtle.
tina = turtle.Turtle()                  

#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
def drawSquare (t, length):
    for i in range(4):
        t.forward(length)
        t.right(90)
def drawTriangle (t, length):
    for i in range(3):
        t.forward(length)
        t.right(120)
def drawCircle(t, length):
    for i in range(36):
        t.forward(length)
        t.right(10)

#   3. Ask the user for the for a shape to draw.
#   4. Draw the appropriate shape depending on their answer (call the right
#      function)
tina.penup()
tina.goto(150,0)
tina.pendown()
drawSquare(tina, 100)
tina.penup()
tina.goto(0,0)
tina.pendown()
drawTriangle(tina, 100)
tina.penup()
tina.goto(-150,0)
tina.pendown()
drawCircle(tina, 10)

turtle.done()
