#Create app using with separating widget
import tkinter
from tkinter import *
from tkinter import ttk
root=Tk()
#App Title
root.title("Python GUI Application ")
ttk.Label(root, text="Separating widget").pack()
#Create Panedwindow
panedwindow=ttk.Panedwindow(root, orient=VERTICAL)
root.resizable(width=False ,height=False)
panedwindow.pack(fill=BOTH, expand=True)
#Fullscreen
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#Create Frams
fram1=ttk.Frame(panedwindow,width=1000,height=600, relief=SUNKEN)
fram2=ttk.Frame(panedwindow,width=1000,height=350, relief=SUNKEN)
panedwindow.add(fram1, weight=1)
panedwindow.add(fram2, weight=4)
#Menu
def quit ():
    root.destroy ()
bar = tkinter.Menu(root)
fileMenu = tkinter.Menu(bar ,tearoff =0)
fileMenu.add_command(label="Exit",command=quit)
bar.add_cascade(label="File",menu=fileMenu)
root.config(menu=bar)
#Calling Main()
root.mainloop()
