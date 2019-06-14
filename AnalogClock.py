import time
import datetime
from turtle import *


bg = Screen()
bg.bgcolor("black")
bg.setup(width =800, height=500)
t1 = Turtle()
bg.tracer(0)


currentDateTime = datetime.datetime.now()

seconds = currentDateTime.second
minutes = currentDateTime.minute
hours = int(time.strftime("%I"))

pen = Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def analogClock(h,m,s,pen):
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)


    #draw the lines

    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)

    #draw hour hand
    pen.penup()
    pen.goto(0,0) #center
    pen.color("white")
    pen.setheading(90) #12 o clock
    angle = (h / 12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(90)

    #draw minutes hand
    pen.penup()
    pen.goto(0,0) #center
    pen.color("gold")
    pen.setheading(90) #12 o clock
    angle = (m / 60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(140) #size of the hand

    #draw seconds hand
    """pen.penup()
    pen.goto(0,0) #center
    pen.color("red")
    pen.setheading(90)
    angle = (s / 60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(170) """#size of the hand
    
while True:
    h = hours
    m = minutes
    s = seconds
        
    analogClock(h,m,s,pen)
    bg.update()
    time.sleep(1)
    pen.clear()


bg.mainloop()         

