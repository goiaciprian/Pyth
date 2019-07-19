#!usr/bin/python

import tkinter as tk
from tkinter import messagebox
import time

score = 0
windowOpen = True
canvasWidth = 750
canvasHeight = 500
leftPressed = 0
rightPressed = 0
batSpeed = 6
ballMoveX = 4
ballMoveY = -4
setBatTop = canvasHeight - 40
setBatBottom = canvasHeight - 30

def on_key_pressed(event):
    global rightPressed
    global leftPressed
    if event.keysym == "Left":
        leftPressed = 1
    elif event.keysym == "Right":
        rightPressed = 1


def on_key_release(event):
    global rightPressed
    global leftPressed
    if event.keysym == "Left":
        leftPressed = 0
    elif event.keysym == "Right":
        rightPressed = 0


def move_bat():
    batMove = batSpeed*rightPressed - batSpeed*leftPressed
    (batLeft, batTop, batRight, batBottom) = canvas.coords(bat)
    if (batLeft > 0 or batMove > 0) and (batRight < canvasWidth or batMove < 0):
        canvas.move(bat, batMove, 0)


def move_ball():
    global ballMoveX
    global ballMoveY
    global score
    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    if ballMoveX > 0 and ballRight > canvasWidth:
        ballMoveX = -ballMoveX
    if ballMoveX < 0 and ballLeft < 0:
        ballMoveX = -ballMoveX
    if ballMoveY < 0 and ballTop < 0:
        ballMoveY = -ballMoveY
    if ballMoveY > 0 and ballBottom > setBatTop and ballBottom < setBatBottom:
        (batLeft, batTop, batRight, batBottom) = canvas.coords(bat)
        if ballRight > batLeft and ballLeft < batRight:
            ballMoveY = -ballMoveY
            score += 1
    canvas.move(ball, ballMoveX, ballMoveY)


def check_game_over():
    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    if ballTop >canvasHeight:
        playAgain = messagebox.askyesno("Game", f" Scorul tau a fost: {score}\nVrei sa joci din nou? ")
        if playAgain:
            reset()
        else:
            close()


def close():
    global windowOpen
    windowOpen = False
    window.destroy()


def reset():
    global leftPressed
    global rightPressed
    global ballMoveX
    global ballMoveY
    global score
    score =0
    leftPressed = 0
    rightPressed = 0
    ballMoveX = 4
    ballMoveY = -4
    canvas.coords(bat, 10, setBatTop, 50, setBatBottom)
    canvas.coords(ball, 20, setBatTop-10, 30, setBatTop)


def main_loop():
    while windowOpen:
        move_bat()
        move_ball()
        window.update()
        time.sleep(0.02)
        if windowOpen:
            check_game_over()


if __name__ == "__main__":    
    window = tk.Tk()
    canvas = tk.Canvas(window, width=canvasWidth, height=canvasHeight, bg="dodgerblue4")
    bat = canvas.create_rectangle(0, 0, 40, 10, fill='dark turquoise')
    ball = canvas.create_oval(0, 0, 10, 10, fill='deep pink')
    canvas.pack()
    window.protocol("WM_DELETE_WINDOW", close)
    window.bind("<KeyPress>", on_key_pressed)
    window.bind("<KeyRelease>", on_key_release)
    reset()
    main_loop()
