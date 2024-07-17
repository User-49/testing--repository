# importing modules
import tkinter
from tkinter import ttk

# creating window
window = tkinter.Tk()
window.title('CALCULATOR -ORBIT')
window.geometry('500x250')


# defining functions
def calculate():
    try:
        display.set(eval(display.get()))
    except SyntaxError or TypeError:
        display.set('an error has occurred')

def back():
    if display.get()=='an error has occurred':
        display.set('')
    else:
        display.set(display.get()[:-1])


# assigning variables
display = tkinter.StringVar()
display.set('')

# creating weights
result = ttk.Label(master=window, textvariable=display, width=30, font='calibri 20', background='white')
buttons_frame = tkinter.Frame(master=window)

buttons_frame.columnconfigure(index=0, weight=2)
buttons_frame.columnconfigure(index=1, weight=2)
buttons_frame.columnconfigure(index=2, weight=2)
buttons_frame.columnconfigure(index=3, weight=1)
buttons_frame.columnconfigure(index=4, weight=1)
buttons_frame.columnconfigure(index=5, weight=1)

_1 = ttk.Button(master=buttons_frame, text='1', command=lambda: display.set(display.get() + '1'))
_2 = ttk.Button(master=buttons_frame, text='2', command=lambda: display.set(display.get() + '2'))
_3 = ttk.Button(master=buttons_frame, text='3', command=lambda: display.set(display.get() + '3'))
_4 = ttk.Button(master=buttons_frame, text='4', command=lambda: display.set(display.get() + '4'))
_5 = ttk.Button(master=buttons_frame, text='5', command=lambda: display.set(display.get() + '5'))
_6 = ttk.Button(master=buttons_frame, text='6', command=lambda: display.set(display.get() + '6'))
_7 = ttk.Button(master=buttons_frame, text='7', command=lambda: display.set(display.get() + '7'))
_8 = ttk.Button(master=buttons_frame, text='8', command=lambda: display.set(display.get() + '8'))
_9 = ttk.Button(master=buttons_frame, text='9', command=lambda: display.set(display.get() + '9'))
_0 = ttk.Button(master=buttons_frame, text='0', command=lambda: display.set(display.get() + '0'))
_decimal = ttk.Button(master=buttons_frame, text='.', command=lambda: display.set(display.get() + '.'))
_add = ttk.Button(master=buttons_frame, text='+', command=lambda: display.set(display.get() + '+'))
_sub = ttk.Button(master=buttons_frame, text='-', command=lambda: display.set(display.get() + '-'))
_mul = ttk.Button(master=buttons_frame, text='x', command=lambda: display.set(display.get() + '*'))
_div = ttk.Button(master=buttons_frame, text='/', command=lambda: display.set(display.get() + '/'))
_equals = ttk.Button(master=buttons_frame, text='=', command=calculate)
_para_open = ttk.Button(master=buttons_frame, text='(', command=lambda: display.set(display.get() + '('))
_para_close = ttk.Button(master=buttons_frame, text=')', command=lambda: display.set(display.get() + ')'))
_back = ttk.Button(master=buttons_frame, text='back', command=back)

_1.grid(column=0, row=0, sticky='we')
_2.grid(column=1, row=0, sticky='we')
_3.grid(column=2, row=0, sticky='we')
_4.grid(column=0, row=1, sticky='we')
_5.grid(column=1, row=1, sticky='we')
_6.grid(column=2, row=1, sticky='we')
_7.grid(column=0, row=2, sticky='we')
_8.grid(column=1, row=2, sticky='we')
_9.grid(column=2, row=2, sticky='we')
_0.grid(column=1, row=3, sticky='we')
_decimal.grid(column=0, row=3, sticky='we')
_add.grid(column=4, row=0, sticky='we')
_sub.grid(column=3, row=1, sticky='we')
_mul.grid(column=5, row=1, sticky='we')
_div.grid(column=4, row=2, sticky='we')
_equals.grid(column=5, row=3, sticky='we')
_para_open.grid(column=3, row=3, sticky='we')
_para_close.grid(column=4, row=3, sticky='we')
_back.grid(column=2, row=3, sticky='we')

# packing weights
result.pack(pady=20)
buttons_frame.pack()

# starting main loop
window.mainloop()

