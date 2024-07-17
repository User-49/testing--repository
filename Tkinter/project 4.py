# importing modules
import tkinter
from tkinter import ttk

# initiating application
window = tkinter.Tk()
window.title('project 4')
window.geometry('600x200')

# defining functions
def prt():
    print(var_1.get())
    var_1.set('button pressed')

# assigning variables
var_1 = tkinter.StringVar(value='start val')

# introducing weights
_1 = ttk.Label(master=window, textvariable=var_1,font='calibri 10 bold')
_2 = ttk.Entry(master=window,textvariable=var_1)
_3 = ttk.Button(master=window,text='print', command = prt)

# packing weights
_1.pack()
_2.pack()
_3.pack()

# starting main loop
window.mainloop()