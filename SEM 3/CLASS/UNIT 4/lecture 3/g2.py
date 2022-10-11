import tkinter as tk
colors = ['red','green','orange','white','yellow','blue']
r = 0
for c in colors:
    tk.Label(text = c, relief = tk.RIDGE, width = 15).grid(row = r, column = 0)
    tk.Entry(bg = c, relief = tk.SUNKEN, width = 10).grid(row = r, column = 1)
    r = r + 1

tk.mainloop()