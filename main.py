from deal_w_tasks import TaskCreator
import tkinter as tk
from button_basics import Buttons
import time

# # # # # # # # # # # # # SETUP # # # # # # # # # # # # #

# Main Variables
SMALLEST = 10
SMALL = 15
NORMAL = 20
LARGE = 25
LARGEST = 30
FONT=("Tekton Pro")
needs_input = True
task_creator = TaskCreator()
button_bg_colour = "#30657a"
window_bg_colour = "#a466b3"

# Screen Setup
top = tk.Tk()
width = top.winfo_screenwidth()
height = top.winfo_screenheight()
top.title("To-Do Today")
top.geometry("%dx%d" % (width - 200, height - 200))
top.maxsize(width, height)
top.configure(bg=window_bg_colour)

# Buttons for task change
tk.Label(top, text=task_creator.current_task(), fg="black", bg=window_bg_colour, padx=10, pady=10, font=(FONT, LARGE)).pack()
skip_btn = tk.Button(text="Skip for now", command=task_creator.skip, background=button_bg_colour, font=(FONT, SMALL)).place(x=300, y=200)
finished_btn = tk.Button(text="Finished!", command=task_creator.finished, background=button_bg_colour, font=(FONT, SMALL)).place(x=200, y=200)
na_btn = tk.Button(text="N/A for Today", command=task_creator.n_a_today, background=button_bg_colour, font=(FONT, SMALL)).place(x=100, y=200)
add_another_btn = tk.Button(text="Add another Task", command=task_creator.ask_input, background=button_bg_colour, font=(FONT, SMALL)).place(x=0, y=200)

if add_another_btn == tk.ACTIVE:
    needs_input = True
if skip_btn == tk.ACTIVE:
    tk.Label(top, text="Saving for later :) Don't be discouraged, keep going! You'll get to it when you can", font=(FONT, SMALL)).pack()
if finished_btn == tk.ACTIVE:
    tk.Label(top, text=task_creator.congrats_phrase(), fg="black", bg=window_bg_colour, font=(FONT, SMALL)).pack()
if na_btn == tk.ACTIVE:
    tk.Label(top, text="Woot Woot! One less thing to worry about today :)", font=(FONT, SMALL)).pack()

top.mainloop()

# # # # # # # # # # # # # ACTUAL CODE # # # # # # # # # # # # #

# while needs_input:
#     task_creator.ask_input()
#     if not task_creator.again():
#         needs_input = False

