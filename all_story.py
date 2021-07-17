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
will have to roll a d20 to see if you were successful in the
acrobatic, strength, intelligent or charismatic feat. If you roll
a 1-10 then you failed your roll but don't worry because you might
not of died even though you most likely would. If you roll a 11-20
then you succeeded and could've been the best outcome in the scenario.

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

k) Koopy, the knucklehead Knight from Kookerry

a) Archemides, the astonishing Archer from Anatolia

w) Willy, the woeful Wizard from Wurstland
    """

    art = "%s\n\n%s\n\n%s" % (fyd_art.smallknight(), fyd_art.smallarcher(), fyd_art.smallwizard())

    answers = {
        'k': 'knight_story.part_1',
        'a': 'archer_story.part_2',
        'w': 'wizard_story.part_3',
    }

    return s,art,answers




