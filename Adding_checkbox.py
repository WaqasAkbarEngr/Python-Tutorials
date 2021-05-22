import tkinter as tki
from tkinter import ttk
win=tki.Tk()
win.title("CheckBox Practice")
statement=ttk.Label(win,text="Choose your option")
statement.grid(column=0,row=0)
check_variable1=tki.IntVar()
chkbx1=ttk.Checkbutton(win,text="Box1",variable=check_variable1)
chkbx1.grid(column=0,row=1,sticky=tki.W)
check_variable2=tki.IntVar()
chkbx2=ttk.Checkbutton(win,text="Box 2",variable=check_variable2)
chkbx2.grid(column=1,row=1,sticky=tki.W)
check_variable3=tki.IntVar()
chkbx3=ttk.Checkbutton(win,text="Box 3",variable=check_variable3)
chkbx3.grid(column=2,row=1,sticky=tki.W)
def chk_action():
    if check_variable1
button=ttk.Button(win,text="None selected")
button.grid(column=0,row=2,columnspan=20)
win.mainloop()