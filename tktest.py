#Create app using with separating widget
from tkinter import *
from tkinter import ttk
root=Tk()
#App Title
root.title("Python GUI Application ")
ttk.Label(root, text="Separating widget").pack()
#Create Panedwindow
panedwindow=ttk.Panedwindow(root, orient=VERTICAL)
panedwindow.pack(fill=BOTH, expand=True)
#Create Frams
fram1=ttk.Frame(panedwindow,width=400,height=300, relief=SUNKEN)
fram2=ttk.Frame(panedwindow,width=400,height=100, relief=SUNKEN)
panedwindow.add(fram1, weight=1)
panedwindow.add(fram2, weight=4)
#Calling Main()
root.mainloop()
