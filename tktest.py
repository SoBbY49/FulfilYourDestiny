# Create app using with separating widget
import tkinter
from tkinter import *
from tkinter import ttk

# root. window
root = Tk()
root.title("Fulfil Your Destiny")
root.configure(bg="black")
root.resizable(width=False, height=False)
# Custom menu
bar = tkinter.Menu(root)
fileMenu = tkinter.Menu(bar, tearoff=0)
fileMenu.add_command(label="Exit", command=quit)
bar.add_cascade(label="File", menu=fileMenu)
root.config(menu=bar)
# FullscreenS
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# ttk.Label(root, text="Fulfil Your Destiny", font=("Courier", 30), background='black', foreground='red').pack()

# Create Panedwindow
# FIXME need to make frames a fixed size
panedwindow_style = ttk.Style()
panedwindow_style.configure("BW.TPanedwindow", foreground="red", background="black", showhandle=False, sashwidth=0)
panedwindow = ttk.Panedwindow(root, orient=HORIZONTAL, style="BW.TPanedwindow")
panedwindow.pack(fill=BOTH, expand=True)

# Create Frams
frame_style = ttk.Style()
frame_style.configure("BW.TFrame", foreground="black", background="black")
fram1 = ttk.Frame(panedwindow, width=1000, height=600, style="BW.TFrame")
fram2 = ttk.Frame(panedwindow, width=1000, height=350, style="BW.TFrame")
panedwindow.add(fram1, weight=1)
panedwindow.add(fram2, weight=4)

# Textbox
sample_text = tkinter.Text(root, height=10)
sample_text.pack()

# Menu
def quit():
    root.destroy()


# Calling Main()
root.mainloop()
