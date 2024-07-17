from tkinter import *

window = Tk()
window.geometry('500x500')
window.title('Project 1')

Label(window, font=('Ariel', 10), text='Project 1').pack(pady=20)

Text(window, font=('Ariel', 10), height=3).pack(padx=10, pady=10)

Entry(window).pack()

Button(window, text='button here', font=('Ariel', 10)).pack(pady=10)

frame = Frame(window)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
Button(frame, text='1').grid(column=0, row=0, sticky='we')
Button(frame, text='2').grid(column=1, row=0, sticky='we')
Button(frame, text='3').grid(column=2, row=0, sticky='we')
Button(frame, text='4').grid(column=0, row=1, sticky='we')
Button(frame, text='5').grid(column=1, row=1, sticky='we')
Button(frame, text='6').grid(column=2, row=1, sticky='we')
Button(frame, text='7').grid(row=2, column=0, sticky='ew')
Button(frame, text='8').grid(row=2, column=1, sticky='ew')
Button(frame, text='9').grid(row=2, column=2, sticky='ew')
Button(frame, text='0').grid(row=3, column=1, sticky='ew')
frame.pack(fill='x')

Button(window, text='Exit', font=('Ariel', 10)).place(x=400, y=450, height=50, width=100)

window.mainloop()
