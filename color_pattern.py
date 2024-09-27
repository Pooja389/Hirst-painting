from turtle import *
import random

turtle = Turtle()
screen = Screen()
screen.setup(width=320,height=330)

turtle.shape("triangle")
turtle.color("red")
turtle.pencolor("red")

turtle.penup()
turtle.goto(-155,-140)
turtle.speed(200)

colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Cyan", "Magenta"]

for i in range(49):

    
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    turtle.dot(20,random.choice(colors))
    

    if i % 6 == 0 and i > 0 and i % 12 != 0:

        turtle.setheading(90)
        turtle.penup()

        turtle.forward(40)
        turtle.dot(20,"blue")
        turtle.setheading(180)
    
    elif i % 12 == 0 and i > 0 and i != 48  :
        turtle.penup()
        turtle.setheading(90)
        turtle.forward(40)
        turtle.dot(20,"blue")
        turtle.setheading(360)


screen.exitonclick()
