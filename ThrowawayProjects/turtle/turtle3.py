import turtle
from time import sleep

##===================
#Window config
turtle.setup(1440, 1080)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("black")


##=================
# Player Turd setup
plyrTurd = turtle.Turtle("turtle")
plyrTurd.color("red")
plyrTurd.spd = 0
plyrTurd.vel = 5
plyrTurd.maxSpd = 40
plyrTurd.trnSpd = 15



##=================
# Event handlers
def holdingUp():
    if plyrTurd.spd < plyrTurd.maxSpd:
        plyrTurd.spd += plyrTurd.vel

    plyrTurd.accelating = True

def releaseUp():
    plyrTurd.accelating = False



def holdingLeft():
    plyrTurd.left(15)

def holdingRight():
    plyrTurd.right(15)

def quit():
    plyrTurd.bye()

def slowDown():
    if plyrTurd.spd >= plyrTurd.vel:
        plyrTurd.spd -= plyrTurd.vel

##================
# Main loop
run = True
while run:

    wn.onkeypress(holdingUp, "Up")
    wn.onkeyrelease(releaseUp, "Up")
    wn.onkeypress(holdingLeft, "Left")
    wn.onkeypress(holdingRight, "Right")
    wn.onkeypress(quit, "q")


    plyrTurd.forward(plyrTurd.spd)
    if plyrTurd.accelating = False:
        #slow
    wn.listen()
