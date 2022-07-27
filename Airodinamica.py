from tkinter import mainloop
import turtle, random
turtle.speed(500)
turtle.pensize(3)
colours = ['green', 'blue', 'red', 'purple', 'white']

x = 1
while x <275:
    turtle.forward(x)
    turtle.right(91)
    c = random.choice(colours)
    turtle.color(colours[x%4])
    x = x+ 1 

mainloop()