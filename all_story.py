"""
All methods here return specific information that is used in game_step
"""
import fyd_art


def intro():
    s = """
                            Welcome to FYD
                            --------------

Read the story carefully. At the end of each part of the story, you
will be presented with multiple options. You will have to choose
which action you take - simply press the key in the keyboard
matching the letter of the action you choose. In some actions you
will have to roll a 20 sided dice to see if you were successful in the
acrobatic, strength, intelligent or charismatic feat. If you roll
a 1-10 then you failed your roll but don't worry because you might
not of died even though you most likely would. If you roll a 11-20
then you succeeded and could've been the best outcome in the scenario.
There are useful commands like changing font size in the menu if needed.

            Choose wisely, for there are no second chances!
                    Your destiny depends on it! 

Do you want to play ?
    y) Yes, bring it on!
    n) No, Im a chicken.

(Simply press y or n to choose) 
    """

    answers = {'y': 'choose_character', 'n': 'quit'}
    return s, fyd_art.fyd_logo_by_line(), answers

def choose_character():

    s = """
------------- CHOOSE YOUR CHARACTER ----------

k) Koron, the knucklehead Knight from Kookaberry

a) Archimedes, the astonishing Archer from Anatolia

w) Wendamyr, the woeful Wizard from Wurstland
    """

    art = "%s" % (fyd_art.smallknight_archer_wizard())

    answers = {
        'k': 'knight_story.part_1',
        'a': 'archer_story.part_1',
        'w': 'wizard_story.part_1',
    }

    return s,art,answers




