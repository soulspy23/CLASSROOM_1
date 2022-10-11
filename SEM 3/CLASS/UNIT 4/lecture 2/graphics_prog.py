#graphic program

import random
import turtle 

color = ['red', 'cyan', 'pink','yellow','green','orange']

t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
length = 100
angle = 50
size = 5
for i in range (length):
    colors = random.choice(color)
    t.pencolor(colors)
    t.fillcolor(colors)
    t.penup()
    t.forward(i + 50)
    t.pendown()
    t.left(angle)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
turtle.exitonclick()