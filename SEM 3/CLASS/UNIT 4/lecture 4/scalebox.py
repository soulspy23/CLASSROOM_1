from tkinter import *

def select():
    set = "value "+ str(v.get)
    label.config(text=set)

top =Tk()
top.geometry('200x100')
v = DoubleVar()
scale = Scale(top, variable=v, from_=1, to=50, orient=HORIZONTAL)
scale.pack()

btn = Button(top, text="Value", command=select)
btn.pack()
label = Label(top)
label.pack()

top.mainloop()