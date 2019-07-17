#!usr/bin/python

import tkinter as tk


lastX, lastY, size = 0, 0, 3
colour = "black"


def store_position(event):
    global lastX, lastY
    lastY = event.y
    lastX = event.x


def on_click(event):
    store_position(event)


def on_drag(event):
    global size
    canvas.create_line(lastX, lastY, event.x, event.y, fill=colour, width=size)
    store_position(event)


def set_red_colour(event):
    global colour, size
    colour = "red"
    size = 3


def black_set_colour(event):
    global colour, size
    colour = "black"
    size = 3


def blue_set_colour(event):
    global colour, size
    colour = "blue"
    size = 3


def yellow_set_colour(event):
    global colour, size
    colour = "yellow"
    size = 3


def white_set_colour(event):
    global colour, size
    colour = "white"
    size = 50


if __name__ == "__main__":
    print("To draw something, hold down the left mouse button and move your mouse around.")
    print("To change your brush colour, click an one of the colours.")

    root = tk.Tk()

    canvas = tk.Canvas(root, width=750, height=500, bg="white")
    canvas.pack()

    red_id = canvas.create_rectangle(10, 10, 30, 30, fill="red")
    black_id = canvas.create_rectangle(10, 35, 30, 55, fill="black")
    blue_id = canvas.create_rectangle(10, 60, 30, 80, fill="blue")
    yellow_id = canvas.create_rectangle(10, 85, 30, 105, fill="yellow")
    white_id = canvas.create_rectangle(10, 110, 30, 130, fill="white")

    canvas.bind("<Button-1>", on_click)
    canvas.bind("<B1-Motion>", on_drag)

    # ! Se sterg patratele din care se aleg culorile
    # TODO Evita stergerea patratelor din care se selecteaza culorile

    canvas.tag_bind(red_id, "<Button-1>", set_red_colour)
    canvas.tag_bind(black_id, "<Button-1>", black_set_colour)
    canvas.tag_bind(blue_id, "<Button-1>", blue_set_colour)
    canvas.tag_bind(yellow_id, "<Button-1>", yellow_set_colour)
    canvas.tag_bind(white_id, "<Button-1>", white_set_colour)

    root.mainloop()
