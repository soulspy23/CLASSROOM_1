from msilib import *
from tkinter import *
def selection():
    selection = "You selected the option "+ str(radio.get())
    label.config(text=selection)

top = Tk()
top.geometry('300x150')
radio = StringVar()
lbl = Label(text = "Favourite Programming Language")
lbl.pack()

r1 = Radiobutton(top, text='Python', variable=radio, value='Python', command=selection)
r1.pack()
r2 = Radiobutton(top, text='C++', variable=radio, value='C++', command=selection)
r2.pack()
r3 = Radiobutton(top, text='Java', variable=radio, value='Java', command=selection)
r3.pack()
r3.select()

label = Label(top)
label.pack()
top.mainloop()