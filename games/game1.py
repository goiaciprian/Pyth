#! usr/bin/python

import turtle as tt
from turtle import Terminator
import random as rd

COLOURS = ["blue", "purple", "cyan", "white", "yellow", "green", "orange"]


def vshape(size):
    tt.right(25)
    tt.forward(size)
    tt.backward(size)
    tt.left(50)
    tt.forward(size)
    tt.backward(size)
    tt.right(25)


def snowflakeArm(size):
    for x in range(0, 4):
        tt.forward(size)
        vshape(size)
    tt.backward(size*4)


def snowflake(size):
    for x in range(0, 10):
        tt.color(rd.choice(COLOURS))
        snowflakeArm(size)
        tt.right(36)

if __name__ == "__main__":

    tt.shape("turtle")
    tt.speed(10)
    tt.pensize(6)
    tt.hideturtle()
    tt.Screen().bgcolor("black")

    try:
        for x in range(0, 3):
            size = rd.randint(5, 30)
            x = rd.randint(-400, 400)
            y = rd.randint(-400, 400)
            tt.penup()
            tt.goto(x, y)
            tt.pendown()
            snowflake(size)
        tt.getscreen()._root.mainloop()
    except Terminator:
        print("exited with exit code 1")
