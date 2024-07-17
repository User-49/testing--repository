import tkinter
from tkinter import ttk
window = tkinter.Tk()
window.title('window 2')
window.geometry('800x200')


def fibonacci():
        try:
            var = int(int_entry.get())
            x, z, y, l = 0, 1, var, list()
            for i in range(y):
                l.append(z)
                x, z = z, z + x
            fibo_list.set(f'FIBONACCI SERIES:\n{l}')
        except ValueError:
            fibo_list.set('    ---INVALID INPUT---\nonly accepts integer values')


fibo_list = tkinter.StringVar()

fibo_label = ttk.Label(master=window,textvariable=fibo_list)
frame_space = ttk.Frame(master=window)
int_entry = ttk.Entry(master=frame_space, width=50)
go_button = ttk.Button(master=frame_space,text='print fibonacci series',command=fibonacci)

frame_space.pack(side='top',pady=12)
int_entry.pack(side='left')
go_button.pack(side='right')
fibo_label.pack(side='top')

window.mainloop()
