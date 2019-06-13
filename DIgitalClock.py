import time
import datetime
from turtle import *


setup()
t1 = Turtle()



currentDateTime = datetime.datetime.now()

seconds = currentDateTime.second
minutes = currentDateTime.minute
hours = currentDateTime.hour


def digitalClock(hours,minutes,seconds):
    while True:
        t1.clear() #to remove overwritting
        t1.color("red")
        t1.write(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2),
                 font = ("arial", 50, "normal"))
        seconds = seconds+1
        time.sleep(1)

        if seconds == 60:
              seconds = 0
              minutes = minutes+1

        if minutes == 60:
              minutes = 0
              hours = hours+1
              
        if hours >= 12:
              hours = hours - 12

digitalClock(hours,minutes,seconds)
