from tkinter import mainloop
import turtle
import time
from pygame import mixer
t = turtle.Turtle()

import turtle
import math

def lovecurve(t):
    x = 16 * (math.sin(t) ** 3)
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x, y

turtle.setup(500, 500)

turtle.title("Love Drawing")
turtle.bgcolor("black")
turtle.pensize(2)
turtle.pencolor("red")
turtle.speed(0)

factor = 20
turtle.penup()
def write(message, pos):
    x,y=pos
    t.penup()
    t.goto(x,y)
    t.color('blue')
    style = ('Stencil Std', 20, 'italic')
    t.write(message, font=style)

write('I', (-68, 95))
write('L', (-55, 95))
write('O', (-42, 95))
write('V', (-30, 95))
write('E', (-14, 95))
write('Y', (10, 95))
write('O', (26, 95))
write('U', (45, 95))

for i in range(0, 400):
    x, y = lovecurve(i)
    turtle.goto(x * factor, y * factor)
    turtle.pendown()
turtle.getcanvas()
postscript = file = "loveddrawing eps"

window = turtle.Screen()
window.bgcolor('black')
window.screensize(500, 500)
window.setup(width=1.0, height=1.0, srartx=None, starty=None)



mainloop()
input()