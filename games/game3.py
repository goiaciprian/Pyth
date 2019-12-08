#!usr/bin/python

import tkinter as tk
import random as rd

gameOver = False
score = 0
squaresToClear = 0
bombfield = []


def play_bombdoger():
    create_bombfield(bombfield)
    window = tk.Tk()
    layout_window(window)
    window.mainloop()


def create_bombfield(bombfield):
    global squaresToClear
    for row in range(0, 10):
        rowList = []
        for column in range(0, 10):
            if rd.randint(1, 100) < 20:
                rowList.append(1)
            else:
                rowList.append(0)
                squaresToClear += 1
        bombfield.append(rowList)


def layout_window(window):
    for rowNumber, rowList in enumerate(bombfield):
        for columnNumber, columnEntry in enumerate(rowList):
            if rd.randint(1, 100) < 25:
                square = tk.Label(window, text="    ", bg='darkgreen')
            elif rd.randint(1, 100) > 75:
                square = tk.Label(window, text="    ", bg="seagreen")
            else:
                square = tk.Label(window, text="    ", bg='green')
            square.grid(row=rowNumber, column=columnNumber)
            square.bind("<Button-1>", on_click)


def on_click(event):
    global score
    global gameOver
    global squaresToClear
    square = event.widget
    row = int(square.grid_info()["row"])
    column = int(square.grid_info()["column"])
    currentText = square.cget("text")
    if not gameOver:
        if bombfield[row][column] == 1:
            gameOver = True
            square.config(bg='red')
            print("Game Over! You hit a bomb!")
            print("Your score was:", score)
        elif currentText == "    ":
            square.config(bg='brown')
            totalbombs = 0
            if row < 9:
                if bombfield[row + 1][column] == 1:
                    totalbombs += 1
            if row > 0:
                if bombfield[row - 1][column] == 1:
                    totalbombs += 1
            if column > 0:
                if bombfield[row][column - 1] == 1:
                    totalbombs += 1
            if column < 9:
                if bombfield[row][column + 1] == 1:
                    totalbombs += 1
            if row > 0 and column > 0:
                if bombfield[row - 1][column - 1] == 1:
                    totalbombs += 1
            if row < 9 and column < 9:
                if bombfield[row + 1][column - 1] == 1:
                    totalbombs += 1
            if row > 0 and column < 9:
                if bombfield[row - 1][column + 1] == 1:
                    totalbombs += 1
            if row < 9 and column > 0:
                if bombfield[row + 1][column + 1] == 1:
                    totalbombs += 1
            square.config(text=" " + str(totalbombs) + " ")
            squaresToClear -= 1
            score += 1

            if squaresToClear == 0:
                gameOver = True
                print("Well Done! You found all the safe squares.")
                print("Your score was: ", score)


if __name__ == "__main__":
    play_bombdoger()
