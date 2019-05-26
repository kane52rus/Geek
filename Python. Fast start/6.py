import turtle
import random

turtle.circle(20)
turtle.speed(0)
answer = ''
while answer != 'N':

    answer = turtle.textinput("Do you wanna exit?","Y/N")
    if answer == 'Y':
        turtle.penup()
        turtle.goto(random.randrange(-300,300), random.randrange(-300,300))
        turtle.pendown()
        turtle.fillcolor(random.random(),random.random(),random.random())
        turtle.begin_fill()
        turtle.circle(random.randrange(1,100))
        turtle.end_fill()
    else:
        pass
