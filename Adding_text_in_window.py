import tkinter as tki
from tkinter import ttk

window=tki.Tk()
window.title("Label Added")
ttk.Label(window,text="Its the added Label").grid(column=0,row=0)
window.mainloop()
