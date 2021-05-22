import tkinter
from tkinter import ttk

number=2
dabba=tkinter.Tk()
dabba.title("Adding Text Box")

label1=ttk.Label(dabba,text="Type anything")
label1.grid(column=0,row=0)

def clicked():
    global number
    button.configure(text="You are "+entered.get())
    button.grid(column=0,row=number)
    number=number+1

entered=tkinter.StringVar()
textbox=ttk.Entry(dabba,width=20,textvariable=entered)
textbox.grid(column=0,row=1)
button=ttk.Button(dabba,text="Enter",command=clicked)
button.grid(column=1,row=1)

dabba.mainloop()