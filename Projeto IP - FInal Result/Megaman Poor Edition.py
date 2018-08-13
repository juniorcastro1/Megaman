import turtle
import time
import math

screen = turtle.Screen()
screen.setup(1280, 720)
mg = turtle.Turtle()
mg.penup()
ruler = turtle.Turtle()


#Stage - creating the ground

ruler.penup()
ruler.speed(0)
ruler.goto(-640, -230)
ruler.pendown()
ruler.fillcolor('grey')
for i in range(2):
    ruler.begin_fill()
    ruler.forward(1300)
    ruler.right(90)
    ruler.forward(500)
    ruler.right(90)
    ruler.end_fill()

    
#Background of the stage

turtle.bgcolor('black')
turtle.bgpic('wilycastle2.gif')

#Adding new shapes

megawalk = 'megawalk.gif'
megawalk1 = 'megawalk1.gif'
megawalk2 = 'megawalk2.gif'
megawalk3 = 'megawalk3.gif'
megaman = 'megastand1.gif'
megaman2 = 'megastand2.gif'
megaprewalk = 'mega2.gif'
megaprewalk2 = 'mega3.gif'
megaarrive = 'megaarrive.gif'
megaarrive2 = 'megaarrive2.gif'
megaarrive3 = 'megaarrive3.gif'
megajump = 'megajump.gif'
megajump2 = 'megajump2.gif'
megaend = 'megaend.gif'
megaend2 = 'megaend2.gif'
megaend3 = 'megaend3.gif'
megadash = 'megadash.gif'



turtle.Screen()

#Registering New Shapes 

turtle.register_shape(megaman)
turtle.register_shape(megaman2)
turtle.register_shape(megawalk)
turtle.register_shape(megawalk1)
turtle.register_shape(megawalk2)
turtle.register_shape(megawalk3)
turtle.register_shape(megaprewalk)
turtle.register_shape(megaprewalk2)
turtle.register_shape(megaarrive)
turtle.register_shape(megaarrive2)
turtle.register_shape(megaarrive3)
turtle.register_shape(megajump)
turtle.register_shape(megajump2)
turtle.register_shape(megaend)
turtle.register_shape(megaend2)
turtle.register_shape(megaend3)
turtle.register_shape(megadash)


#-----------------------------------

mg.shape(megaman)
turtle.listen()
mg.speed(1)

#Megaman Arriving

mg.speed(0)
mg.goto(-620, 600)
mg.speed(1)
mg.shape(megaarrive)
mg.goto(-620, -215)
mg.shape(megaarrive2)
time.sleep(0.1)
mg.shape(megaarrive3)
time.sleep(0.1)
mg.shape(megaman)

#Defining functions

def right():
    mg.shape(megaprewalk)
    time.sleep(0.1)
    mg.shape(megawalk)
    time.sleep(0.1)
    mg.fd(20)
    time.sleep(0.1)
    mg.shape(megawalk2)
    time.sleep(0.1)
    mg.shape(megaman)
    

def left():
    mg.shape(megaprewalk2)
    time.sleep(0.1)
    mg.shape(megawalk1)
    time.sleep(0.1)
    mg.bk(20)
    time.sleep(0.1)
    mg.shape(megawalk3)
    time.sleep(0.1)
    mg.shape(megaman2)
    
def up():
    mg.shape(megajump)
    mg.speed(0)
    mg.left(90)
    mg.speed(1)
    mg.fd(50)
    mg.speed(0)
    mg.right(180)
    mg.speed(1)
    mg.fd(50)
    mg.speed(0)
    mg.left(90)
    mg.speed(1)
    mg.shape(megaman)

def pulo():
    mg.shape(megajump)
    mg.speed(0)
    mg.right(90)
    mg.speed(1)
    mg.circle(50, -180)
    mg.speed(0)
    mg.right(90)
    mg.speed(1)
    mg.shape(megaman)

def pulotras():
    mg.shape(megajump2)
    mg.speed(0)
    mg.left(90)
    mg.speed(1)
    mg.circle(50, 180)
    mg.speed(0)
    mg.left(90)
    mg.speed(1)
    mg.shape(megaman2)

def dash():
    mg.shape(megadash)
    mg.forward(50)
    time.sleep(0.2)
    mg.shape(megaman)
    

#Keyboard bindings
    
turtle.onkey(right,'Right')
turtle.onkey(left,'Left')
turtle.onkey(up,'Up')
turtle.onkey(dash,'Down')
turtle.onkey(pulo, 's')
turtle.onkey(pulotras, 'a')

#Ending - Megaman goes home

while True:
    mg.forward(0)

    if mg.xcor() > -200:
        mg.speed(1)
        time.sleep(1)
        mg.shape(megaend)
        time.sleep(0.5)
        mg.shape(megaend2)
        time.sleep(0.5)
        mg.shape(megaend3)
        time.sleep(1)
        mg.shape(megaarrive3)
        time.sleep(0.2)
        mg.shape(megaarrive2)
        time.sleep(0.2)
        mg.shape(megaarrive)
        mg.goto(-200, 1500)



