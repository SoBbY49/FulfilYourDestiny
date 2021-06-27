# Create app using with separating widget
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.font import Font

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
# Fullscreen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# ttk.Label(root, text="Fulfil Your Destiny", font=("Courier", 30), background='black', foreground='red').pack()

# Create Panedwindow
# FIXME need to make frames a fixed size
panedwindow_style = ttk.Style()
panedwindow_style.configure("BW.TPanedwindow", foreground="red", background="black", showhandle=False, sashwidth=0)
panedwindow = ttk.Panedwindow(root, orient=HORIZONTAL, style="BW.TPanedwindow")
panedwindow.pack(fill=BOTH, expand=True)

# Create text areas

art_font = Font(family="Courier",size=50)
story_font = Font(family="Courier",size=20)

txt_art = tkinter.Text(panedwindow,state = "normal", foreground="white", background="black")
txt_story = tkinter.Text(panedwindow,state = "normal", foreground="white", background="black")
panedwindow.add(txt_art, weight=1)
panedwindow.add(txt_story, weight=4)

txt_art.insert(END," art here")
txt_story.insert(END,"this is the story of the 3 piggies")
txt_story.insert("1.0","FYD starts here...")

# disabling to stop user editing
txt_art.configure(state="disabled")
txt_story.configure(state="disabled")
# Textbox
sample_text = tkinter.Text(root, height=10)
sample_text.pack()


# Quit
def quit():
    root.destroy()


# NOTHING WILL HAPPEN AFTER CALLING mainloop() UNTIL THE WINDOW IS CLOSED
root.mainloop()
