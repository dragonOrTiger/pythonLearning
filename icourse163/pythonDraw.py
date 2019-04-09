"""
setup(width=0.5, height=0.75, startx=None, starty=None)
Set the size and position of the main window.
Arguments:
    width: as integer a size in pixels, as float a fraction of the Default is 50% of
    height: as integer the height in pixels, as float a fraction of the Default is 75% of
    startx: if positive, starting position in pixels from the left edge of the screen, if negative from the right edge Default, startx=None is to center window horizontally.
    starty: if positive, starting position in pixels from the top edge of the screen, if negative from the bottom edge edge of the screen, if negative from the bottom edge
Example:
    setup (width=200, height=200, startx=0, starty=0)
    sets window to 200x200 pixels, in upper left of screen
    setup(width=.75, height=0.5, startx=None, starty=None)
    sets window to 75% of screen by 50% of screen and centers
    
penup()
Pull the pen up -- no drawing when moving.
Aliases: penup | pu | up

fd(distance)
Aliases: forward | fd
Argument: distance -- a number (integer or float)
Move the turtle forward by the specified distance, in the direction the turtle is headed.

pendown()
Pull the pen down -- drawing when moving.
Aliases: pendown | pd | down

pensize(width=None)
Set or return the line thickness.
Aliases:  pensize | width
Argument: width -- positive number
Set the line thickness to width or return it. If resizemode is set to "auto" and turtleshape is a polygon, that polygon is drawn with the same line thickness. If no argument is given, current pensize is returned.

pencolor(*args)
Return or set the pencolor.
Arguments:
Four input formats are allowed:
- pencolor()
    Return the current pencolor as color specification string,possibly in hex-number format (see example).May be used as input to another color/pencolor/fillcolor call.
- pencolor(colorstring)
    s is a Tk color specification string, such as "red" or "yellow"
- pencolor((r, g, b))
    *a tuple* of r, g, and b, which represent, an RGB color, and each of r, g, and b are in the range 0..colormode, where colormode is either 1.0 or 255
- pencolor(r, g, b)
    r, g, and b represent an RGB color, and each of r, g, and b are in the range 0..colormode
If turtleshape is a polygon, the outline of that polygon is drawn with the newly set pencolor.

seth(to_angle)
Set the orientation of the turtle to to_angle.
Aliases:  setheading | seth
Argument: to_angle -- a number (integer or float)
Set the orientation of the turtle to to_angle. Here are some common directions in degrees:
standard - mode:          logo-mode:
    -------------------|--------------------
       0 - east                0 - north
      90 - north              90 - east
     180 - west              180 - south
     270 - south             270 - west

circle(radius, extent=None, steps=None)
Draw a circle with given radius.
Arguments:
    radius -- a number
    extent (optional) -- a number
    steps (optional) -- an integer
Draw a circle with given radius. The center is radius units left of the turtle; extent - an angle - determines which part of the circle is drawn. If extent is not given, draw the entire circle. If extent is not a full circle, one endpoint of the arc is the current pen position. 
Draw the arc in counterclockwise direction if radius is positive, otherwise in clockwise direction. 
Finally the direction of the turtle is changed by the amount of extent.
As the circle is approximated by an inscribed regular polygon, steps determines the number of steps to use. If not given, it will be calculated automatically. Maybe used to draw regular polygons.
"""
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
"""
print(turtle.position())
print(turtle.heading())
turtle.circle(300, steps=3)
turtle.circle(300, steps=4)
turtle.circle(300, steps=5)
turtle.circle(300, steps=6)
turtle.circle(300)
print(turtle.position())
print(turtle.heading())
"""
turtle.done()

