#/usr/bin/python
import turtle
import math
turtle.setup(1.0, 1.0)
turtle.penup()
turtle.fd(-350)
turtle.pensize(8)
turtle.pencolor("purple")
turtle.pendown()
for i in range(5):
    turtle.fd(2 * 280 * math.sin(math.radians(72)))
    turtle.right(144)
turtle.left(72)
#turtle.fd(30)
turtle.circle(-280)
ts = turtle.getscreen()
ts.getcanvas().postscript(file="star.eps")
turtle.done()
