import turtle

turtle.setup(1024, 768)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("black")             # Set the background color
plyrTurd = turtle.Turtle()               # Create player turtle
plyrTurd.color("green")
plyrTurd.shape("turtle")
plyrTurd.pu()
plyrTurd.speed(0)
plyrTurd.setpos(-200,0)
plyrTurd.pd()

# The next four functions are our "event handlers".
def h1():
   plyrTurd.forward(30)

def h2():
   plyrTurd.left(90)

def h3():
   plyrTurd.right(90)

def h4():
    wn.bye()                        # Close down the turtle window

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

compTurd = turtle.Turtle()
compTurd.color("red")

def redShape():
    compTurd.forward(100)
    compTurd.left(56)
    wn.ontimer(redShape, 500)

spiralTurd = turtle.Turtle()
spiralTurd.color("blue")
spiralSize = 90

def blueSpiral():
    global spiralSize
    for x in range(3):
        spiralTurd.forward(spiralSize)
        spiralTurd.left(100)
    spiralSize+=10
    wn.ontimer(blueSpiral(), 500)


#wn.ontimer(redShape, 500)
wn.ontimer(blueSpiral(), 500)

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()
