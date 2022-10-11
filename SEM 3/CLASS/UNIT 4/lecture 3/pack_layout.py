import tkinter as tk

root = tk.Tk()

w = tk.Label(root, text ="Red Sun", bg = "red", fg = "white")
w.pack()
w = tk.Label(root, text ="Green Grass", bg = "green", fg = "black")
w.pack(padx = 5, pady = 20, side = tk.LEFT)
w = tk.Label(root, text ="Blue Sky", bg = "blue", fg = "black")
w.pack(fill = tk.X, padx = 10, pady = 10, ipadx = 60, ipady = 60)

tk.mainloop()