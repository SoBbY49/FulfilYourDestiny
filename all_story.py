"""
All methods here return specific information that is used in game_step
"""
import fyd_art


def intro():
    s = """
Welcome to FYD lalb bla blah
------- -- --- -- --- ----- -

Read the story carefully. At the end of each part of the story, you will be presented with options.
You will have to choose which action you take - simply press the key in the keyboard matching the letter of the action you choose. 

Choose wisely, for there are no second chances - your destiny depends on it! 

Do you want to play ?

Y) Yes, bring it on!
N) Not now, i am a chicken.

( Simply press Y or N to choose ) 
    """

    answers = {'y': 'choose_character', 'n': 'quit'}
    return s, fyd_art.fyd_logo_by_line(), answers

def choose_character():

    s = """
------------- CHOOSE YOUR CHARACTER ----------

A) Archemides, the astonishing Archer from Anatolia

k) Koopy, the knucklehead Knight from Kookerry

w) Willy, the woeful Wizard from Wurstland

q) Quokquok, the quitting Chicken
    """

    art = "%s\n\n%s\n\n%s" % (fyd_art.archer(), fyd_art.knight() , fyd_art.wizard())

    answers = {
        'w': 'wizard_start',
        'k':'knight_story.part_1',
        'a' : 'archer_story.archer1',
        'q' : 'quit'
    }

    return s,art,answers




