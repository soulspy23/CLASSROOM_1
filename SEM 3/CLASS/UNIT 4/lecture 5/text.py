import tkinter as tk
from tkinter import *

def NextQuote():
    quote = "\nTime is Money !"
    t.insert(tk.END,quote)

win = Tk()
win.geometry('250x250')

#to create a text widget and specify size
t = Text(win, height=6, width=53)

#to create label
l = Label(win, text="Quote for the day")
l.config(font=("Courier",14))

Quote = "Cleanliness is next to Godliness"

b1 = Button(win, text="Next", command=NextQuote)
b2 = Button(win, text="Exit", command=win.destroy)

l.pack()
t.pack()
b1.pack()
b2.pack()

#insert quote
t.insert(tk.END,Quote)
tk.mainloop()