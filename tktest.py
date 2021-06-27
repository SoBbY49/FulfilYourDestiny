# Create app using with separating widget
import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()

# App Title
root.title("Python GUI Application ")
root.configure(bg="black")
ttk.Label(root, text="Fulfil Your Destiny", font=("Courier", 30), background='black', foreground='red').pack()

# Create Panedwindow
panedwindow = ttk.Panedwindow(root, orient=VERTICAL)
root.resizable(width=False, height=False)
panedwindow.pack(fill=BOTH, expand=True)

# Fullscreen
# FIXME you can't see this in alt tab or task bar...
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# FIXME: define text style for the app and use in all objects if possible
# Create Frams
style = ttk.Style()
style.configure("BW.TFrame", foreground="black", background="black")
fram1 = ttk.Frame(panedwindow, width=1000, height=600, relief=SUNKEN, style="BW.TFrame")
fram2 = ttk.Frame(panedwindow, width=1000, height=350, relief=SUNKEN, style="BW.TFrame")

panedwindow.add(fram1, weight=1)
panedwindow.add(fram2, weight=4)

# Text
sample_text = tkinter.Text(root, height=10)
sample_text.pack()

# Menu
def quit():
    root.destroy()


bar = tkinter.Menu(root)
fileMenu = tkinter.Menu(bar, tearoff=0)
fileMenu.add_command(label="Exit", command=quit)
bar.add_cascade(label="File", menu=fileMenu)
root.config(menu=bar)

# Calling Main()
root.mainloop()
