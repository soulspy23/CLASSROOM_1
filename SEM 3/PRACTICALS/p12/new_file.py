from tkinter import *
from tkinter.filedialog import askopenfilename

def NewFile():
    print("New File!")

def OpenFile():
    name = askopenfilename()
    print(name)

def About():
    print("This is a simple example of a menu")

myWindow = Tk()
menu = Menu(myWindow)
myWindow.config(menu=menu)
filemenu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()

sub_menu = Menu(filemenu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')
filemenu.add_cascade(
    label="Preferences",
    menu=sub_menu
)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=myWindow.quit)
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
mainloop()