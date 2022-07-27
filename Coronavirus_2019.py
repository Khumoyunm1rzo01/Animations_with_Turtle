from turtle import *
import turtle
color("green")
bgcolor("black")
speed(11)
hideturtle()
b = 0
t = turtle.Turtle()
while b < 200:
    right(b)
    forward(b * 3)
    b = b + 1
turtle.mainloop()
