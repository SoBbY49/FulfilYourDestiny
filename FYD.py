# Create app using with separating widget
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from fyd_art import *

# number of seconds to wait before starting the game, after the main screen is up
lag_to_start = 1
counter = 0

"""
Updates text of a text box
If insert_where is None, we replace the whole text. Otherwise use it as the position to insert it in.
"""
def set_text(my_textbox, text, insert_where = None ) :

    # enabling because otherwise we can't change text
    my_textbox.configure(state="normal")

    if insert_where == None:
        my_textbox.delete(1.0,"end")
        my_textbox.insert(1.0, text)
    else:
        my_textbox.insert(insert_where, text)

    # disabling to stop user editing
    my_textbox.configure(state="disabled")

# Replace content of art panel
def set_art(art):
    set_text(txt_art, art)

# Replace content of story panel
def set_story(story):
    set_text(txt_story, story)

# adds text to story box
def add_story(story):
    set_text(txt_story, story, 'end')

# adds text to art box
def add_art(art):
    set_text(txt_art, art, 'end')

# inserts text to story where we tell it.
# defaults to insert at start of story
def insert_story(story, insert_where = 1.0):
    set_text(txt_story, story, insert_where)

# inserts text to art where we tell it.
# defaults to insert at start of art
def insert_art(art, insert_where = 1.0):
    set_text(txt_art, art, insert_where)



def start_fyd():
    global counter

    # get the story started
    set_art( fyd_logo())
    # txt_art.insert(END, fyd_logo())
    # txt_art.insert("1.0", chicken())
    set_story( "this is the story of the 3 piggies")

    insert_story("...and the lone wolf")
    # txt_story.insert("1.0", "FYD starts here...")


    counter += 1
    prog.configure(text = "STARTED - %d" % ( counter) )

# root. window
root = Tk()
root.title("Fulfil Your Destiny")
root.configure(bg="black")
root.resizable(width=False, height=False)
root.wm_attributes('-fullscreen', True)

# Custom menu
bar = tkinter.Menu(root)
fileMenu = tkinter.Menu(bar, tearoff=0)
fileMenu.add_command(label="Exit", command=quit)
bar.add_cascade(label="File", menu=fileMenu)
root.config(menu=bar)
# Fullscreen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Create Panedwindow
# FIXME need to make frames a fixed size
panedwindow_style = ttk.Style()
panedwindow_style.configure("BW.TPanedwindow", foreground="red", background="black", showhandle=False, sashwidth=0)
panedwindow = ttk.Panedwindow(root, orient=HORIZONTAL, style="BW.TPanedwindow")
panedwindow.pack(fill=BOTH, expand=True)

# Create text areas
art_font = Font(family="Courier", size=50)
story_font = Font(family="Courier", size=20)

txt_art = tkinter.Text(panedwindow, state="normal", foreground="white", background="black", width=100, height=20)
txt_story = tkinter.Text(panedwindow, state="normal", foreground="white", background="black", width=100, height=20)
panedwindow.add(txt_art, weight=1)
panedwindow.add(txt_story, weight=1)

# Textbox
sample_text = tkinter.Text(root, height=10)
sample_text.pack()

prog = tkinter.Label(root,height=1)
prog.configure(text='Loading...')
prog.pack(fill="x")

# Quit
def quit():
    root.destroy()


root.after(lag_to_start * 1000, start_fyd)
# NOTHING WILL HAPPEN AFTER CALLING mainloop() UNTIL THE WINDOW IS CLOSED
root.mainloop()