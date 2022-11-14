import tkinter as tk

BUTTON_BG_COLOUR = "#30657a"
WINDOW_BG_COLOUR = "#a466b3"
SMALLEST = 10
SMALL = 15
NORMAL = 20
LARGE = 25
LARGEST = 30
FONT=("Tekton Pro")


class Buttons(tk):

    def __init__(self):
        super().__init__()
        self.Button(background = BUTTON_BG_COLOUR)
        self.Button(font=(FONT, SMALL))
