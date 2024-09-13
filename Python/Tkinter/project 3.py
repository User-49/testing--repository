import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title('Converter (kilometers to miles)')
window.geometry('1000x500')


def calculate():
    miles = miles_input.get()
    kilometers.set(f'OUTPUT: {miles * 1.61}')

miles_input= tkinter.IntVar()
kilometers = tkinter.StringVar()

label_1 = tkinter.ttk.Label(master=window, text='Kilometer -->  miles', font='Calibri 20')
frame_1 = tkinter.ttk.Frame(master=window)
frame_input = tkinter.ttk.Entry(master=frame_1, textvariable=miles_input)
frame_button = tkinter.ttk.Button(master=frame_1, text='GO', command=calculate)
output = tkinter.ttk.Label(master=window, textvariable=kilometers, font='Calibri 15')

label_1.pack(side='top', pady=0)
frame_input.pack(side='left', padx=10)
frame_button.pack(side='right')
frame_1.pack(pady=10)
output.pack()


window.mainloop()
