from turtle import *
t = [Turtle(), Turtle()]
c = [1, 3]
x = 2

bgcolor("black")
speed(0)
delay(0)
tracer(10)
ht()

for index, i in enumerate(t):
    i.color("white")
    i.ht()
    i.speed(0)
    i.width(3)
    i.pu()
    i.seth(90)
    i.bk(x * 60 * (c[index]))
    i.seth(0)
    i.pd()

colors = ["darkorange1", "gold", "cyan", "pink", "red", "blue"]
for i in colors:
    t[0].color(i)
    t[1].color(i)
    color(i)
    for i in range(361):
        for i in range(6):
            t[0].fd(x)
            t[0].lt(1)
        pu()
        goto(t[0].pos())
        t[1].fd(c[1] * x)
        t[1].lt(1)
        pd()
        speed(0)
        goto(t[1].pos())

done()
mainloop()