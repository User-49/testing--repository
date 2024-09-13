import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title('Buttons')
window.geometry('500x500')

button_str = tkinter.StringVar()
simple_button = ttk.Button(master=window,text='this is a simple button',command=lambda:print('you pressed a simple button',textvariable=button_str))


simple_button.pack()

window.mainloop()