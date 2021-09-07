import fyd_art
import dice_roll


def part_1():
    s = """
You wake up to find yourself in darkness.
You try to feel around but all you can feel is the cold ground and hear some water dripping.
As your eyes start to adjust to the darkness you look around once more and come face to face with a skeleton.
You jump back and see that it is wearing shackles, ‘How did I get here?’.
You get up and as you try to find a way out you accidentally stub your toe on a large stick, ow.
You pick it up and you see that it has a large gem on the top of it, you start handling it to see how it feels.
It seemed to you to be a magic staff, how you knew that even you don’t know.
You look back at the skeleton and get some shivers down your spine.
You squint your eyes and see some writing scratched into the wall next to it.
You walk close to it and read it out loud.
“Say... fireball?” FOOOOSH, there's a sudden burst of light as a large ball of fire emerges on the gem from the top of the staff you are holding.
You thrust the staff towards the only door and only way out you can find and the entrance explodes open.
You peek your head out and see bookshelf after bookshelf in the room before you.
You head to the books and start reading them, many not making sense to you at first you start to understand the cryptic language in which these books are written in.
You read a few pages and realise that it's a spell book, the page you’re reading is titled ‘Invisibility’.
As you continue to read the page you hear multiple pairs of footsteps coming towards you from a set of stairs.

    What do you do?
        a) You quickly run to the stairs, ready to bonk anyone on the head with your staff.
        b) Cast fireball.
        c) Cast invisibility.
    """
    answers = {'a': 'wizard_story.part_1a', 'b': 'wizard_story.part_1b', 'c': 'wizard_story.part_1c'}
    return s, fyd_art.wizard(), answers



def part_1a():
    s = """
You hide behind a bookshelf that is right next to the staircase and hold the staff above your head.
Two peasants walk down the stairs behind a very large shrouded man with a large axe in both hands.
You hear one of the peasants whisper to the other peasant, `Oh no, the wizard has escaped.’.
You sneak up behind them and whack one of the peasants over the head.
He falls to the ground and the other peasant sees you and points at you with a shaky hand.
It seems like he is trying to talk but no words are coming out of his mouth.
You hit him across the head with your staff and he falls over.
As you look towards the large man with the large axe you see that he is face to face with you.

    What do you do?
        a) Whack him across the face with your staff.
        b) Cast fireball.
        c) Cast invisibility.
    """
    answers = {'a': 'wizard_story.part_1aa', 'b': 'wizard_story.part_1ab', 'c': 'wizard_story.part_1ac'}
    return s, fyd_art.wizard(), answers


def part_1aa():
    s = """
You swing your staff against the man's head.
The amount of force you put into the swing shatters the staff, the wood explodes.
The large gem that was on top of the staff falls the the ground.
The man doesn't even flinch or look affected by the blow.
The man picks the gem up and crushes it in his hand, he opens his hand and pours the gem that is now sand onto the ground.
    
    %s""" % (fyd_art.you_died())
    answers = {'a': 'wizard_story.part_1aa'}
    return s, fyd_art.largeman(), answers


def part_1ab():
    s = """
You say fireball and once again a ball of fire emerges from the gem on your staff.
You thrust it into the man's chest and an explosion erupts.
You're blown backwards onto the stairs and the man gets launched into the wall.
He falls onto his knees and you can see the giant hole that he has made in the wall.
He shakily gets up using the large axe and starts walking limping towards you.
You run up the stairs.

    y) Continue?
    """
    answers = {'y': 'wizard_story.part_2b'}
    return s, fyd_art.wizard(), answers


def part_2b():
    s = """
As you reach the top of the stairs you see a large open door that leads to outside.
You begin running to it but you suddenly hear rumbling.
You turn around and you see the large man walking up the stairs using the large axe to help stabilise himself after the huge blast.

    What do you do?
        a) Cast fireball.
        b) Cast invisibility.
        c) Attack him with the staff.
    """
    answers = {'a': 'wizard_story.part_2ba', 'b': 'wizard_story.part_2bb', 'c': 'wizard_story.part_2bc'}
    return s, fyd_art.largeman(), answers


def part_2ba():
    diceresult = dice_roll.rolld20()
    if diceresult < 11:
        s = """
You cast fireball as a large ball of fire emerges on the top of the staff.
You thrust the staff forward as the fireball flies towards the man.
The fireball flies at the large man but he is able to move out of the way in time for the ball of fire to explode against the wall.
The man begins to charge at you.
        %s""" % (fyd_art.you_died())

        art = "Unlucky roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = {}
    else:
        s = """
You cast fireball as a large ball of fire emerges on the top of the staff.
You thrust the staff forward as the fireball flies towards the man.
The fireball flies to fast for the large man to dodge as it smashes into his face.
The room bursts in flames and once the flames disappear you see a a large figure now burnt to a crisp.

    y) Continue?
        """

        art = "Woah nice roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = {'y': 'wizard_story.part_2a'}
    return s, art, answers


def part_2bb():
    s = """
You cast invisibility and you vanish, the man now enraged starts swinging his axe everywhere trying to find you.
He begins destroying everything in the room and you quickly run outside into freedom.

    y) Continue?
    """
    answers = {'y': 'wizard_story.part_2a'}
    return s, fyd_art.largeman(), answers


def part_2bc():
    s = """
You swing your staff against the man's head.
The amount of force you put into the swing shatters the staff, the wood explodes.
The large gem that was on top of the staff falls the the ground.
The man doesn't even flinch or look affected by the blow.
The man picks the gem up and crushes it in his hand, he opens his hand and pours the gem that is now sand onto the ground.
    %s""" % (fyd_art.you_died())

    answers = {}
    return s, fyd_art.wizard(), answers



def part_1ac():
    s = """
You say disappear and you become invisible.
The man suddenly swings his giant axe at where you were but you manage to move out of the way.
The man starts destroying everything in the room trying to find you.
You creep up the stairs out of the room.

    y) Continue?
    """
    answers = {'y': 'wizard_story.part_2a'}
    return s, fyd_art.largeman(), answers


def part_1b():
    s = """
You hide behind one of the bookshelves far away from the stairs.
You peek from behind the bookshelf and see two peasants behind a very large shrouded man with a large axe in his hands.
You jump into view and thrust your magic staff towards them, the large ball of fire whizzes just past the large man but explodes right next to the two peasants.
An explosion erupts and the peasants are incinerated, the blast from the fireball had caught the large man's hood and cloak on fire.
He chucks the cloak off of him and you can now see his inhumanly large muscles, he begins to charge at you.

    What do you do?
        a) Jump out of his way
        b) Cast invisibility.
    """
    answers = {'a': 'wizard_story.part_1ba', 'b': 'wizard_story.part_1bb'}
    return s, fyd_art.wizard(), answers


def part_1ba():
    diceresult = dice_roll.rolld20()
    if diceresult <11:
        s = """
You try to jump out of the way but you trip over your leg and fall to the ground.
The man runs at you and slices his axe down onto you.
        
        %s""" % (fyd_art.you_died())

        art = "Unlucky roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = {}
    else:
        s = """
You manage to jump out of the man's way in time and he slices the bookshelves that were near you in half.
He wasn't able to slow down in time and runs through the bookshelves into the wall.
The room shakes and parts of rock start to fall down from the ceiling.
You run towards the stairs hoping to get out of the room before the room collapses.
The man locks onto you and charges you once again.
You manage to get up the stairs before he runs into the staircase turning the stairs to rubble.
You see the huge rocks fall from the staircase onto the man and it goes quiet.

    y) Continue?
        """

        art = "Woah nice roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = {'y': 'wizard_story.part_2a'}
    return s, art , answers


def part_1bb():
    s = """
You say disappear and you become invisible.
The man keeps charging to where you were and smashes into the bookshelves.
The man starts destroying everything in the room trying to find you.
You creep up the stairs out of the room.

    y) Continue?
    """
    answers = {'y': 'wizard_story.part_2a'}
    return s, fyd_art.wizard(), answers


def part_1c():
    s = """
Not needing to hide, you stand out in the open and see two peasants and a very large shrouded man holding a huge axe come down the stairs.
They walk right past you towards the small dungeon cell you were locked in.
The large man looks at the exploded door and sees that you’re not inside the cell.
The peasants start getting worried and start shaking, the large man mutters to the peasants ‘Find the wizard’.
The peasants nod their heads worryingly and hurry up the stairs.
The large man sits down on a chair in the room and starts to sharpen his large axe.
You just remembered that there was nothing in the spell book which told you how long the invisible spell would last.

    What do you do?
        a) Keep standing there, you can probably stay invisible for a long time...right?
        b) Go upstairs.
    """
    answers = {'a': 'wizard_story.part_1ca', 'b': 'wizard_story.part_1cb'}
    return s, fyd_art.wizard(), answers


def part_1ca():
    s = """
You keep standing there and observing the man as he keeps sharpening his axe.
The man is insanely muscly, he doesn't even look human.
The man suddenly looks up and stares right at you.
You look down at yourself and see that you are no longer invisible.
The man gets of his chair and throws the huge axe at you, slicing you down the middle.
    
    %s""" % (fyd_art.you_died())
    answers = {'a': 'wizard_story.part_1ca'}
    return s, fyd_art.you_died(), answers


def part_1cb():
    s = """
The man keeps sharpening his axe on the chair and you creep towards the stairs and make your way up.
As soon as you get out of view of the room you begin to see your hands again.
The invisibility spell just ran out, that was close.

    y) Continue?
    """
    answers = {'y': 'wizard_story.part_2a'}
    return s, fyd_art.wizard(), answers


def part_2a():
    s = """
Congratulations, you've successfully made it out of the dungeon!
You have finished the wizards story as best as possible.
Are you ready to go back to the real world?

    y) I'm ready!
    """
    answers = {'y': 'quit'}
    return s, fyd_art.youwon(), answers