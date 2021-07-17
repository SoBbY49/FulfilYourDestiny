import fyd_art
import dice_roll


def part_2():
    s = """
    ‘Bang bang bang bang’, your eyes open suddenly as you feel your face on the cold stone floor you are lying on.
    You look at where the banging is coming from and you see a guard hitting his sword against the metal bars of the cell you are lying in.
    ‘I'm in prison?’, you get up and try to remember why and how you ended up in prison but you don’t remember why.
    You look across the hallway to another person in a prison cell sitting cross legged staring at you.
    ‘Uhh excuse me… do you know how I got here?’.
    The person doesn't respond, they only point to a room with a closed door and a large key hole being guarded by two prison guards.
    A guard starts opening everyone's doors and even that door.
    As you are about to get out of view of the door everyone stops walking, you look to the front of the line and see a brawl has broken out.
    Prison guards start pushing through the crowd of prisoners and you see that the prison guards guarding the door have left and have started walking past you.
    As one of the guards walk past you you see that one of them has a large golden key attached to their waist.
    You lightly grab hold of it and slip it out from their belt buckle.
    You creep backwards toward the door and manage to put the key into the keyhole and get inside.
    You look around and see that the room is full of weapons and armor, your eyes dart to a dagger, a bow and a bunch of arrows in a quiver.
    As you finish equipping the bow and arrow and your dagger in your pocket you turn around to leave but you see a guard at the door holding a sword staring at you.
        What do you do?
        a) You pull out your bow and shoot at him.
        b) You take out your dagger and run at him.
        c) You play dumb and tell the guard that you thought this was the cafeteria.
    """
    answers = {'a': 'archer_story.part_2a', 'b': 'archer_story.part_2b', 'c': 'archer_story.part_2c'}
    return s, fyd_art.archer(), answers


def part_2a():
    s = """
    You quickly pull your bow out and fire two arrows at the guard.
    The guard doesn't have time to react and was hit by the two arrows in the chest.
    The guard starts to fall to the ground
    You run over to him to try and attempt to grab him before he hits the ground but his body falls and slumps to the floor with a loud THUD.
    You hear a couple of guards shout ‘What was that’ and ‘Let’s go check it out’, you start to hear their footsteps approaching the room.
        What do you do?
        a) Hide and leave the guards body on the floor.
        b) Hide the guards body but not yourself.
    """
    answers = {'a': 'archer_story.part_2aa', 'b': 'archer_story.part_2ab'}
    return s, fyd_art.archer(), answers


def part_2aa():
    diceresult = dice_roll.rolld20()
    if diceresult <11:
        s = """
        You attempt to hide but your heart starts beating faster and faster as you hear the pair of footsteps coming close.
        The two guards enter the room and they see you in the middle of the room with the guards body on the floor.
        They run at you with their swords.
        YOU DIED
        """

        art = "Unlucky roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = {}
    else:
        s = """
        You hide behind the door and leave the guards body on the floor as you hear a pair of footsteps walk towards your room.
        The two guards see the body and sound the alarm, you hear guards shouting that a prisoner is loose.
        The guards pick up the body and take it away.
        It's going to be pretty hard to escape now.
        """

        art =  "Woah nice roll!!\n\n\n%s" % (fyd_art.d20(diceresult))
        answers = {'a': 'archer_story.part_2aa'}
    return s, art, answers


def part_2ab():
    s = """
    You put the guards body under the pile of weapons and wait behind the pile of weapons for the guards to come inside.
    The two guards enter and you pull out your bow and fire an arrow at one of the guards.
    It goes through his head and he falls to the ground.
    You stand up pull out your dagger, the guard starts to run out of the room but you throw your dagger at him.
    It slices into his neck and he falls against the wall in the hallway.
    You walk over to him and take your dagger back, you begin to find a way out. 
    """
    answers = {'a': 'archer_story.part_2ab'}
    return s, fyd_art.archer(), answers


def part_2b():
    s = """
    You run at the guard as fast as you can and pull out your dagger.
    The guard swings his sword at you and you slide on your knees underneath it.
    You thrust your dagger into the guard's chest and stab him multiple times.
    You grab his limp body and pull it inside and hide it underneath the weapons.
        What do you do?
        a) Leave the room and go the way all the other prisoners went.
        b) Put on the guards clothes and go the way all the other prisoners went.
    """
    answers = {'a': 'archer_story.part_2ba', 'b': 'archer_story.part_2bb'}
    return s, fyd_art.archer(), answers


def part_2ba():
    s = """
    You exit the room and make your way towards the prisoners.
    You walk past the cells that everyone was being held in, you eventually walk past the cell you were held in.
    Across form your cell is the prisoner that told you where to go, he is still in his cell.
    There are guards surrounding him and he is being beaten.
    The prisoner is in a ball being kicked, you can see his face.
    He opens his eyes and looks at you.
    The guards don't know you are there yet.
    """
    answers = {'a': 'archer_story.part_2ba'}
    return s, fyd_art.archer(), answers


def part_2bb():
    s = """
    You exit the room and make your way towards the prisoners.
    You walk past the cells that everyone was being held in, you eventually walk past the cell you were held in.
    Across form your cell is the prisoner that told you where to go, he is still in his cell.
    There are guards surrounding him and he is being beaten.
    The prisoner is in a ball being kicked, you can see his face.
    He opens his eyes and looks at you, it seems like he knows that its you even though you are in disguise.
    The guards see you, thinking that you are also a guard they tell you to join in.
    """
    answers = {'a': 'archer_story.part_2bb'}
    return s, fyd_art.archer(), answers


def part_2c():
    s = """
    The guard starts to walk to you menacingly, ‘Put the weapons away’ he tells you angrily.
    You put your hands up in the air to try and show no sign of danger to the guard and as he gets closer to you he punches you across the face.
    He takes the bow and the arrows off of you but he doesn't realise that you have a dagger in your pocket.
    You stand up and he starts to put handcuffs on your wrists, 'Don't try anything funny' he says.
        What do you do?
        a) Before he can put the handcuffs completely on your wrists you pull you dagger out of your pocket and attack him.
        b) Let him put handcuffs on your wrists.
    """
    answers = {'a': 'archer_story.part_2ca', 'b': 'archer_story.part_2cb'}
    return s, fyd_art.archer(), answers


def part_2ca():
    diceresult = dice_roll.rolld20()
    if diceresult <11:
        s = """
        You pull your hand away from the handcuffs but not quick enough because the guard has the sword pointed at your face.
        'I said not to try anything funny' he tells you.
        YOU DIED
        """

        art = "Unlucky roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = {}
    else:
        s = """
        
        You manage to pull your hand away from the handcuffs and pull out your dagger.
        You slash the knife at the guard and it slices his throat.
        You put his body under the pile of weapons and you get ready to leave the room.
        """

        answers = {'a': 'archer_story.part_2ca'}
    return s, art, answers


def part_2cb():
    s = """
    The guard puts the handcuffs on you and walks you out of the room and takes you the way that all the prisoners went.
    As you walk past your cell you see the prisoner that told you where to find your weapons, hes being beaten.
    There are a few guards kicking him as he is huddled on the floor.
    With your wrists still in handcuffs you dislocate both your thumbs and slip your hands through the handcuffs.
    You drop your handcuffs and the guard walking you looks down at them, you pul your dagger out and slice his throat. 
    """
    answers = {'a': 'archer_story.part_2cb'}
    return s, fyd_art.archer(), answers
