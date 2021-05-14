import turtle             # allows us to use the turtles library
wn = turtle.Screen()      # creates a graphics window     #sadly, it is not supported in cmd.exe
wn.bgcolor("lightgreen")
veer = turtle.Turtle()    # create a turtle named veer
veer.forward(150)         # tell veer to move forward by 150 units
veer.left(90)             # turn by 90 degrees
veer.color("blue")        # make veer blue
veer.pensize(3)
veer.speed(10)            #speed ranges from 1 lowest to high 10, but 0 means no animation, hence fastest
wn.exitonclick()
#you can make multiple turtles too

#you can store -
veer.price = 500

#We could also write turtle.Screen() to make a new window for our turtles to paint in.

#also
distance = 50
for _ in range(10):
    elan.forward(distance)
    elan.right(90)
    distance = distance + 10

#A turtle’s pen can be picked up or put down.
#This allows us to move a turtle to a different place without drawing a line. The methods are up and down.
#Note that the methods penup and pendown do the same thing.

alex.up()
alex.forward(100)     # this moves alex, but no line is drawn
alex.down()

#Every turtle can have its own shape. The ones available “out of the box” are arrow, blank, circle, classic, square, triangle, turtle.
alex.shape("turtle")

#A turtle can “stamp” its footprint onto the canvas
#stamping works even when the pen is up.

#here's how you can make a spiral
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

dist = 5
tess.up()                     # this is new
for _ in range(30):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(dist)          # move tess along
    tess.right(24)              # and turn her
    dist = dist + 2
wn.exitonclick()



#color with argument color name  Changes the color of the turtle’s tail
#fillcolor with argument color name  Changes the color of the turtle will use to fill a polygon
#heading   Returns the current heading
#position  Returns the current position
#goto with argument x,y  Move the turtle to position x,y
#begin_fill  Remember the starting point for a filled polygon
#end_fill  Close the polygon and fill with the current fill color
#dot   Leave a dot at the current position
#stamp Leaves an impression of a turtle shape at the current location
#shape with arg. shapename  Should be ‘arrow’, ‘triangle’, ‘classic’, ‘turtle’, ‘circle’, or ‘square’
