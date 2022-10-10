#message box

from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("300x150")

def click():
    messagebox.showinfo("Hello","Green button clicked")

a = Button(top, text = "Yellow", activeforeground = "black", activebackground = "yellow", pady = 10)
b = Button(top, text = "Blue", activeforeground = "white", activebackground = "blue", pady = 10)
c = Button(top, text = "Green", activeforeground = "black", activebackground = "green", pady = 10)
d = Button(top, text = "Red", activeforeground = "white", activebackground = "red", pady = 10)

#pack geometry
a.pack(side = BOTTOM)
b.pack(side = RIGHT)
c.pack(side = TOP)
d.pack(side = LEFT)

top.mainloop()