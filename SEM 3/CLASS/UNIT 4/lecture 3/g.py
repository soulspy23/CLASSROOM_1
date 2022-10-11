from tkinter import *
root = Tk()
root.geometry('300x300')
for x in range(10):
    for y in range(6):
        entry = Entry(root, width = 6)
        entry.grid(row = x, column = y)

root.mainloop()