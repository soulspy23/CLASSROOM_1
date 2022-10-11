#menu bar

from tkinter import *
top =Tk()
def hello():
    print("Hello !")

#create toplevel menubar
menubar = Menu(top)
menubar.add_command(label = "Hello", command=hello)
menubar.add_command(label = "Quit", command=quit)

#display menu
top.config(menu=menubar)
top.mainloop()