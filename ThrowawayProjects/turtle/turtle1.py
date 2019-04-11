import turtle
turtle.setup(1440, 1080)

def drawRect(turt, x, y = -1):
    if y == -1:
        for i in range(4):
            turt.forward(x)
            turt.left(90)

    else:
        for i in range (2):
            turt.forward(x)
            turt.left(90)
            turt.forward(y)
            turt.left(90)

#Function to initialize game.
#The turtles are called turds because I'm a child
def startGame(*turds):

    for turd in turds:
        turd.clear()


wn = turtle.Screen()
alex = turtle.Turtle()


##Event Handles
def space():
    startGame(alex, writer)


wn.title("Turtle soup, wonderful turtle soup!")
wn.bgcolor("black")

#Set up box drawing turtle
alex.color("green")
alex.shape("turtle")

alex.pu()
alex.speed(0)
alex.setpos(-500,0)

alex.pd()
alex.speed(4)

# Setup writer turtle
writer = turtle.Turtle()
writer.ht()
writer.pu()
writer.speed(0)

writer.color("red")


#Title Screen Setup
drawRect(alex, 1000, 400)

writer.setpos(0, 200)
writer.write("TURTLE CANNIBALISM:", False, "center", ("Lucida Console", 60, "bold"))
writer.setpos(0,100)
writer.write("A videogame documentary", False, "center", ("Lucida Console", 30, "bold"))
writer.setpos(0,50)
writer.write("inspired by totes real events", False, "center", ("Lucida Console", 30, "bold"))
writer.setpos(0, -300)
writer.write("Press ENTER to begin", False, "center", ("Lucida Console", 30, "bold"))

#inspired by real events

wn.onkey(startGame, "q")

# The next four functions are our "event handlers".
def h1():
   alex.forward(30)

def h2():
   alex.left(45)

def h3():
   alex.right(45)

def h4():
    wn.bye()


# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

wn.listen()
wn.mainloop()
