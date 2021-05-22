import tkinter as tkin
from tkinter import ttk

win_box=tkin.Tk()
win_box.title("Drop Down Menu Creation")

ask_birthday=ttk.Label(win_box,text="Enter your birthday")
ask_birthday.grid(row=0,column=0)

day=tkin.StringVar()
select_day=ttk.Combobox(win_box,textvariable=day,state='readonly')
select_day.grid(row=1,column=0)
select_day['values']=("Select Day",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
select_day.current(0)

month=tkin.StringVar()
select_month=ttk.Combobox(win_box,textvariable=month)
select_month.grid(row=1,column=1)
select_month['values']=('Select Month','January','February','March','April','May','June','July','August','September','October','November','December')
select_month.current(0)

year=tkin.StringVar()
select_year=ttk.Entry(win_box,text="Select Year",textvariable=year)
select_year.grid(row=1,column=2)

win_box.mainloop()