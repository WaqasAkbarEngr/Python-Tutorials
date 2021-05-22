import tkinter as tki
from tkinter import ttk

clicks=0
window=tki.Tk()
window.title("Adding a Button")
# window.resizable(800,600)

first_label=ttk.Label(window,text="Label 1")
first_label.grid(column=0,row=0)

def clicked():
    global clicks
    clicks=clicks+1
    button.configure(text="Clicks ("+str(clicks)+")")

def resetit():
    button.configure(text="Button")
    global clicks
    clicks=0

button=ttk.Button(window,text="Button",command=clicked)
button.grid(column=1,row=0)
reset=ttk.Button(window,text="Reset",command=resetit)
reset.grid(column=2,row=0)

window.mainloop()