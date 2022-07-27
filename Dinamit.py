from turtle import *

bgcolor('black')
speed(0)
hideturtle()
for i in range(10000):
    color('cyan')
    circle(i)
    color('orange')
    color('blue')
    circle(i*0.8)
    right(3)
    forward(3)
done()