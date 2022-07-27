import colorsys
from turtle import *

speed(0)
bgcolor('black')

n = 300
h = 0


for i in range(60):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    color(c)

    forward(200)
    right(90)
    forward(200)
    right(90)
    forward(200)
    right(90)
    forward(200)

    right(96)

for i in range(60):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    color(c)

    forward(200)
    right(90)
    forward(200)
    right(90)
    forward(200)
    right(90)
    forward(200)

    right(96)

for i in range(60):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    color(c) 

    forward(300)
    right(90)
    forward(300)
    right(90)
    forward(300)
    right(90)
    forward(300)

    right(96)

for i in range(60):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    color(c)

    forward(500)
    right(90)
    forward(500)
    right(90)
    forward(500)
    right(90)
    forward(500)

    right(96)

done()
mainloop()
input()