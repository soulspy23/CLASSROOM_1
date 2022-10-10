from tkinter import *
window =Tk()

#widgets
window.title('Hello SYBCA')
window.geometry("300x200+10+20")

#adding button
b = Button(window, text = "Submit")
b.pack() #using pack geometry
window.mainloop()