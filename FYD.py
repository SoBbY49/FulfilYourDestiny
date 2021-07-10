# Create app using with separating widget
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from fyd_art import *

# Definitions for general game stuff (startup, final, etc)
from all_story import *
# Definitions for knight path
import knight_story
# definitions for archer path
import archer_story
import wizard_story

# Quit
def quit():
    root.destroy()

def game_step(name_of_step):
    """
    Loads the step of the game, defined in name_of_step.

    name_of_step is a method we are going to call that will give us the information we need to do all the things.
    The step we call must return some things in specific order that we use here to make the game work

    Basically, the game flow is:
    game_step(something):
    - set art txt
    - set story txt
    - define options to choose from
    - define next steps for options (names for functions that art part_in_story)
    - handle response
    - go to the next game_step (as decided by choice) ^^

    FIXME : there are some special cases we want to handle on key press.. ie, when selecting character, we want to set the game_state['character']... here or in keypress?
            game_State[stage] = intro can be useful?

    """
    # handy variables - matching the order of results from the method that defines the next step
    # ie, result[0] == the story
    _story = 0 # string
    _art = 1 # string
    _answers = 2 # dictionary

    # Get information about the step we are in
    step_info = eval( name_of_step + '()')

    # if we called quit, the window was destroyed and there is no more game. So dont do anything
    if name_of_step != 'quit':

        # Show the story and art
        set_story(step_info[_story])
        set_art(step_info[_art])

        # Update the game state
        global game_state # We are using the global game_state var.

        game_state['next_step'] = step_info[_answers]
        game_state['valid_answers'] = ''
        # go over the answers that this step accepts and save the keys that i want to accept for the key press handler
        for answer in list(step_info[_answers]):
            game_state['valid_answers'] = game_state['valid_answers'] + answer


def keyPressedHandler(my_event):
    """Event handler for any key pressed.
    This is where we check what the player chose and keep the game moving forward.

    Reference: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/event-handlers.html
    """

    # Check if None just in case.
    # Shift and control give '', I dont care about those
    if my_event.char is not None and my_event.char != '':

        is_valid_answer = False

        # check if the key pressed is a valid answer. The valid answers for this part of story in game_state['valid_answers']
        # walk the valid answers and check each of them
        for valid_answer in game_state['valid_answers']:
            # compare uppercase to uppercase because we cant check for capslock
            if my_event.char.upper() == valid_answer.upper():
                is_valid_answer = True
                break # exit the loop, found an answer

        if is_valid_answer:
            question_label['text'] = 'VALID ANSWER DETECTED! %s ' % ( my_event.char)
            # Go to the right next step
            game_step(game_state['next_step'][my_event.char])
        else:
            question_label['text'] = '"%s" is not a valid answer. Valid answers are one of [%s]' % ( my_event.char, game_state['valid_answers'])

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

########## Main section ##########

# Global variables
# State of the game - initial values
game_state= {} # a dictionary
game_state['character'] = 'none_yet' # FIXME needed? useful?
game_state['current_step'] = 'intro'  # FIXME needed ?
game_state['next_step'] = {} # This holds another dictionary


# Creating the game GUI
root = Tk()
root.title("Fulfil Your Destiny")

# Custom menu
bar = tkinter.Menu(root)
fileMenu = tkinter.Menu(bar, tearoff=0)
fileMenu.add_command(label="Exit", command=quit)
bar.add_cascade(label="File", menu=fileMenu)
root.config(menu=bar)

screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

root_width= int(screenwidth * 0.9)
root_height= int(screenheight * 0.9)

top_panel_height = int(root_height * 0.96)

root_geometry = '%dx%d+%d+%d' % (root_width, root_height, (screenwidth - root_width) / 2, 0)
root.geometry(root_geometry)
root.configure(bg='black')
root.resizable(width=False, height=False)
root.iconphoto(True, PhotoImage(file='icons8-icosahedron-96.png'))

# ----- frames ----------
# top frame for art + story
top_container = Frame(root,borderwidth=0,height=top_panel_height)

top_container.pack(side='top',fill='both', expand=True, pady=0, padx=0)
top_container.grid_rowconfigure(0,weight=1)
top_container.grid_columnconfigure(0,weight=1)
top_container.grid_columnconfigure(1,weight=1)
top_container.grid_propagate(False)

# Bottom frame for question and answer
bottom_container = Frame(root,borderwidth=0,bg='black',height=(root_height-top_panel_height))

bottom_container.pack(side='bottom',fill='both', expand = True)
bottom_container.grid_rowconfigure(0,weight=1)
bottom_container.grid_columnconfigure(0,weight=1)
bottom_container.grid_columnconfigure(1,weight=1)
bottom_container.grid_propagate(False)

# ----- text boxes ----------
main_txt_config = {'foreground': "white", 'background' : "black", 'state':'normal', 'height': top_panel_height, 'border': 0}
font_art = Font(family="Courier", size=15)
font_story = Font(family="Courier", size=15)

# Passing the default config. Each one has a different font, so we pass this too
txt_art = Text(top_container, font = font_art, **main_txt_config)
txt_art.grid(row=0,column=0,sticky='nw')

txt_story = Text(top_container, font = font_story, **main_txt_config)
txt_story.grid(row=0,column=1,sticky='ne')

# ----------
question_label = Label(bottom_container)
question_label.grid(row=0,column=0,sticky='e')
question_label.configure(font=Font(family="Helvetica", size=18) , fg='red' )
question_label['text'] = 'Choose your action!'

# Catch all key presses
root.bind('<KeyRelease>', keyPressedHandler)

game_step('intro')

# NOTHING WILL HAPPEN AFTER CALLING mainloop() UNTIL THE WINDOW IS CLOSED
root.mainloop()