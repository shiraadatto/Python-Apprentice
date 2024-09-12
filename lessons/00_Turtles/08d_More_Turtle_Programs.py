"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section " Click on the Turtle"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and when you click on it, it moves to a random location on the screen.

Use this code to get a random x and y location


    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

"""
import turtle as turtle
import random

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()
t.penup()
t.shape("turtle")

t.turtlesize(stretch_wid=10, stretch_len=10, outline=4)

def turtle_clicked(t, x, y):
    print('turtle clicked!')
    
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    print(x,y)
    t.goto(x,y)

t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))

turtle.done() # Important! Use `done` not `exitonclick` to keep the window open