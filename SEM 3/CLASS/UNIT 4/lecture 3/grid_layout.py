import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

b1 = tk.Button(frame, text ="Button 1")
b1.grid(row = 0, column = 0, padx = 5, pady = 5)
b2 = tk.Button(frame, text ="Button 2")
b2.grid(row = 0, column = 1, padx = 5, pady = 5)
b3 = tk.Button(frame, text ="Button 3")
b3.grid(row = 1, column = 0, padx = 5, pady = 5)
b4 = tk.Button(frame, text ="Button 4")
b4.grid(row = 1, column = 1, padx = 5, pady = 5)
b5 = tk.Button(frame, text ="Click here to proceed")
b5.grid(row = 2, column = 0, padx = 5, pady = 5,columnspan = 2)

root.mainloop()