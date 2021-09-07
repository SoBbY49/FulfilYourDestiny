import fyd_art
import dice_roll


def part_1():
    s = """
‘Bang bang bang bang’, your eyes open suddenly as you feel your face
 on the cold stone floor you are lying on.
You look at where the banging is coming from and you see a guard
 hitting his sword against the metal bars of the cell you are lying in.
‘I'm in prison?’, you get up and try to remember why and how you ended
 up in prison but you don’t remember why.
You look across the hallway to another person in a prison cell
 sitting cross legged staring at you.
‘Uhh excuse me… do you know how I got here?’.
The person doesn't respond, they only point to a room with a closed
 door and a large key hole being guarded by two prison guards.
A guard starts opening everyone's doors and even that door.
As you are about to get out of view of the door everyone stops
walking, you look to the front of the line and see a brawl has broken
 out.
Prison guards start pushing through the crowd of prisoners and you see
 that the prison guards guarding the door have left and have started
  walking past you.
As one of the guards walk past you you see that one of them has a
 large golden key attached to their waist.
You lightly grab hold of it and slip it out from their belt buckle.
You creep backwards toward the door and manage to put the key into
 the keyhole and get inside.
You look around and see that the room is full of weapons and armor,
 your eyes dart to a dagger, a bow and a bunch of arrows in a quiver.
As you finish equipping the bow and arrow and your dagger in your
 pocket you turn around to leave but you see a guard at the door holding a sword staring at you.

    What do you do?
        a) You pull out your bow and shoot at him.
        b) You take out your dagger and run at him.
        c) You play dumb and tell the guard that you thought this was the cafeteria.
    """
    answers = {'a': 'archer_story.part_1a', 'b': 'archer_story.part_1b', 'c': 'archer_story.part_1c'}
    return s, fyd_art.archer(), answers


def part_1a():
    s = """
You quickly pull your bow out and fire two arrows at the guard.
The guard doesn't have time to react and was hit by the two arrows in
 the chest.
The guard starts to fall to the ground
You run over to him to try and attempt to grab him before he hits the
 ground but his body falls and slumps to the floor with a loud THUD.
You hear a couple of guards shout ‘What was that’ and ‘Let’s go check
 it out’, you start to hear their footsteps approaching the room.

    What do you do?
        a) Hide and leave the guards body on the floor.
        b) Hide the guards body but not yourself.
    """
    answers = {'a': 'archer_story.part_1aa', 'b': 'archer_story.part_1ab'}
    return s, fyd_art.archer(), answers


def part_1aa():
    diceresult = dice_roll.rolld20()
    if diceresult <11:
        s = """
You attempt to hide but your heart starts beating faster and faster
 as you hear the pair of footsteps coming close.
The two guards enter the room and they see you in the middle of the
 room with the guards body on the floor.
They run at you with their swords.

%s""" % (fyd_art.you_died())

        art = "Unlucky roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = {}
    else:
        s = """
You hide behind the door and leave the guards body on the floor as you
 hear a pair of footsteps walk towards your room.
The two guards see the body and sound the alarm, you hear guards
 shouting that a prisoner is loose.
The guards pick up the body and take it away.

    y) Continue?
        """

        art = "Woah nice roll!!\n\n\n%s" % (fyd_art.d20(diceresult))
        answers = {'y': 'archer_story.part_2a'}
    return s, art, answers


def part_1ab():
    s = """
You put the guards body under the pile of weapons and wait behind
 the pile of weapons for the guards to come inside.
The two guards enter and you pull out your bow and fire an arrow
 at one of the guards.
It goes through his head and he falls to the ground.
You stand up pull out your dagger, the guard starts to run out of
 the room but you throw your dagger at him.
It slices into his neck and he falls against the wall in the hallway.
You walk over to him and take your dagger back, you begin to find
 a way out.

    y) Continue?
    """
    answers = {'y': 'archer_story.part_2a'}
    return s, fyd_art.archer(), answers


def part_2a():
    s = """
You walk the opposite way from the other prisoners trying to look
 for a way out.
You continue walking down the corridor until you see a room with
 five guards inside.
The door is open and you peak inside, the five guards are talking
 and there is a large door behind them.
'That must be the way out' you think.

    What do you do?
        a) Run at them with your dagger in hand.
        b) Shoot them from afar.
    """
    answers = {'a': 'archer_story.part_2aa', 'b': 'archer_story.part_2ab'}
    return s, fyd_art.guards(), answers


def part_2aa():
    s = """
You run at the guards with ready to stab them with your dagger.
They don't see you at first and you manage to kill the two that
 were closest to you.
The three other guards now see you and charge at you with their
 swords.
You lunge at one of them and stab him in the neck but the other
 two guards come from either side of you.
They thrust their swords and stab you.
You fall to the ground.
    
    %s""" % (fyd_art.you_died())
    answers = {}
    return s, fyd_art.archer(), answers


def part_2ab():
    diceresult = dice_roll.rolld20()
    if diceresult <11:
        s = """
You begin firing arrows at the guards but you can't fire fast enough
 as they begin running at you.
You try to pull out your dagger in time but one of the guards slices
 down and cuts your arm off.
%s""" % (fyd_art.you_died())

        art = "Unlucky roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = {}
    else:
        s = """
You aim at guards and wait for one to walk behind the other.
As son as they do you fire, the arrow pierces through the first
 guards neck and gets stuck in the second guard.
They both fall to the ground and the three guards begin running
 towards you.
You quickly fire one more arrow and you kill one more, you then
 pull out your dagger.
You run at the two guards and stab one in the chest, the other
 guard swings at you.
You manage to dodge the sword and stab him in the neck.
You walk towards the large door and open it.
Freedom
    y) Continue?
        """
        art = "Woah nice roll!!\n\n\n%s" % (fyd_art.d20(diceresult))
        answers = {'y': 'archer_story.part_3a'}
    return s, art, answers


def part_1b():
    s = """
You run at the guard as fast as you can and pull out your dagger.
The guard swings his sword at you and you slide on your knees 
underneath it.
You thrust your dagger into the guard's chest and stab him multiple 
times.
You grab his limp body and pull it inside and hide it underneath the
 weapons.

    What do you do?
        a) Leave the room and go the way all the other prisoners went.
        b) Put on the guards clothes and go the way all the other prisoners went.
    """
    answers = {'a': 'archer_story.part_1ba', 'b': 'archer_story.part_1bb'}
    return s, fyd_art.archer(), answers


def part_1ba():
    s = """
You exit the room and make your way towards the prisoners.
You walk past the cells that everyone was being held in, you eventually
 walk past the cell you were held in.
Across form your cell is the prisoner that told you where to go, he is
 still in his cell.
There are guards surrounding him and he is being beaten.
The prisoner is in a ball being kicked, you can see his face.
He opens his eyes and looks at you.
The guards don't know you are there yet.
    
    What do you do?
        a) Sneak up on them and kill them with your dagger.
        b) Shoot them with your bow from afar.
    """
    answers = {'a': 'archer_story.part_1baa', 'b': 'archer_story.part_1bab'}
    return s, fyd_art.archer(), answers


def part_1baa():
    s = """
You sneak up to them and manage to get into the cell with them.
The man being beaten looks over at you and stares into your eyes.
You grab your dagger and stab them oth in the back of their neck.
They fall to the floor and the man gets up.
He nods at you and starts to walk away, you decide to follow him.
He starts walking the opposite way of the prisoners and you realise
 that that's the way out.
You continue walking down the corridor until you see a room with five
 guards inside.
The door is open and you peak inside, the five guards are talking and
 there is a large door behind them.

    y) Continue?
    """
    answers = {'y': 'archer_story.part2b'}
    return s, fyd_art.guards(), answers


def part_1bab():
    s = """
You hide behind the wall and aim your bow and arrow at the guards.
You shoot one and it lands in his neck and he falls to the ground.
The other ground jumps up and is about to shout out for help but 
you manage to shoot him in the chest.
He falls over to the ground and the man walks over to you.
He looks at you and nods and starts walking behind you, you decide to 
follow him.
He starts walking the opposite way of the prisoners and you realise 
that that's the way out.
You continue walking down the corridor until you see a room with 
five guards inside.
The door is open and you peak inside, the five guards are talking
 and there is a large door behind them.

    y) Continue?
    """
    answers = {'y': 'archer_story.part2b'}
    return s, fyd_art.guards(), answers


def part_2b():
    s = """
The man looks at you waiting for you to do something.
It seems like he will do anything to escape.

    What do you do?
        a) Let him stay back and you fight them.
        b) Get him to help you fight them.
    """
    answers = {'a': 'archer_story.part_2ba', 'b': 'archer_story.part_2bb'}
    return s,fyd_art.archer(), answers


def part_2ba():
    s = """
You aim at guards and wait for one to walk behind the other.
As son as they do you fire, the arrow pierces through the first guards
 neck and gets stuck in the second guard.
They both fall to the ground and the three guards begin running towards
 you.
You quickly fire one more arrow and you kill one more, you then pull 
out your dagger.
You run at the two guards and stab one in the chest, the other guard 
swings at you.
You manage to dodge the sword and stab him in the neck.
The man walks next to you and you both open the door.
Freedom

    y) Continue?
    """
    answers = {'y': 'archer_story.part_3b'}
    return s, fyd_art.archer(), answers


def part_2bb():
    s = """
You give the man your dagger and runs into the room.
You start firing arrows at the guards and you take out two of them.
The man is able to stab one in the neck and is about to kill another 
one.
The guard swings his sword and cuts the man's throat, you shoot an 
arrow and kill that guard.
You run over to the man, pick up your dagger and kill the last guard.
You kneel down next to him and he just stares at you.
He's dead.
You walk over to the door and open it.
You look back at the man and walk out.

    y) Continue?
    """
    answers = {'y': 'archer_story.part_3c'}
    return s, fyd_art.archer(), answers


def part_1bb():
    s = """
You exit the room and make your way towards the prisoners.
You walk past the cells that everyone was being held in, you eventually 
walk past the cell you were held in.
Across form your cell is the prisoner that told you where to go, he is 
still in his cell.
There are guards surrounding him and he is being beaten.
The prisoner is in a ball being kicked, you can see his face.
He opens his eyes and looks at you, it seems like he knows that its you 
even though you are in disguise.
The guards see you, thinking that you are also a guard they tell you to 
join in.

    What do you do?
        a) Join in.
        b) Kill the guards.
    """
    answers = {'a': 'archer_story.part_1bba', 'b': 'archer_story.part_1bbb'}
    return s, fyd_art.archer(), answers


def part_1bba():
    s = """
Being peer pressured you start joining in and start to kick the man.
The man looks at you in the eyes and you feel a sense of guilt.
You pull out your dagger and stab both guards as they fall to the 
ground.
The man gets up and stares at you, he doesn't seem very thankful.
He starts walking behind you, you decide to follow him.
He's walking the opposite way of the prisoners and you realise that 
that's the way out.
You continue walking down the corridor until you see a room with 
five guards inside.
The door is open and you peak inside, the five guards are talking 
and there is a large door behind them.

    y) Continue?
    """
    answers = {'y': 'archer_story.part_2c'}
    return s, fyd_art.guards(), answers


def part_1bbb():
    s = """
The guards are still waiting for you to join in but you quickly pull 
out your dagger.
You stab them both in the neck and they fall to the ground, the man 
gets up of the floor.
He looks at you and nods and starts walking behind you, you decide 
to follow him.
He starts walking the opposite way of the prisoners and you realise 
that that's the way out.
You continue walking down the corridor until you see a room with 
five guards inside.
The door is open and you peak inside, the five guards are talking 
and there is a large door behind them.

    y) Continue?
    """
    answers = {'y': 'archer_story.part_2c'}
    return s, fyd_art.guards(), answers


def part_2c():
    s = """
The man looks at you waiting for you to do something.
It seems like he will do anything to escape.

    What do you do?
        a) Pretend to be a guard and bring the man with you to help kill the guards.
        b) Pretend to be a guard but get the man to wait while you kill the guards.
    """
    answers = {'a': 'archer_story.part_2ca', 'b': 'archer_story.part_2cb'}
    return s, fyd_art.archer(), answers


def part_2ca():
    s ="""
You give the man your dagger and he hides it behind his back
You walk into the room while holding the man by the collar.
The guards laugh at the man and one punches him to the floor as he 
falls out of your grip.
The man now enraged uses the dagger to stab the guard in his chest.
You pull out your bow quickly from its holster.
You start firing arrows at the guards and you take out two of them.
The man is able to stab one in the neck and is about to kill another
 one.
The guard swings his sword and cuts the man's throat, you shoot an 
arrow and kill that guard.
You run over to the man, pick up your dagger and kill the last guard.
You kneel down next to him and he just stares at you.
He's dead.
You walk over to the door and open it.
You look back at the man and walk out.

    y) Continue?
    """
    answers = {'y': 'archer_story.part_3c'}
    return s, fyd_art.archer(), answers


def part_2cb():
    s = """
You walk into the room and the guards do not suspect a thing.
You manage to trick a few guards into looking the other way while 
you slice the other guards throats.
You have done this to three guards until the other two guards see 
their dead bodies.
You pull out your bow and fire two arrows rapidly.
They both fall to the ground.
The man walks next to you and you both open the door.
Freedom

    y) Continue?
    """
    answers = {'y': 'archer_story.part_3b'}
    return s, fyd_art.archer(), answers


def part_1c():
    s = """
The guard starts to walk to you menacingly, ‘Put the weapons away’ 
he tells you angrily.
You put your hands up in the air to try and show no sign of danger 
to the guard and as he gets closer to you he punches you across the face.
He takes the bow and the arrows off of you but he doesn't realise 
that you have a dagger in your pocket.
You stand up and he starts to put handcuffs on your wrists
, 'Don't try anything funny' he says.

    What do you do?
        a) Attack him with the handcuffs on your wrists
        b) Let him put handcuffs on your wrists.
    """
    answers = {'a': 'archer_story.part_1ca', 'b': 'archer_story.part_1cb'}
    return s, fyd_art.archer(), answers


def part_1ca():
    diceresult = dice_roll.rolld20()
    if diceresult <11:
        s = """
You pull your hand away from the handcuffs but not quick enough because
 the guard has the sword pointed at your face.
'I said not to try anything funny' he tells you.

%s""" % (fyd_art.you_died())

        art = "Unlucky roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = {}
    else:
        s = """ 
You manage to pull your hand away from the handcuffs and pull out your 
dagger.
You slash the knife at the guard and it slices his throat.
You put his body under the pile of weapons and you get ready to leave 
the room.

    y) Continue?
    """
        art = "Woah nice roll!!\n\n\n%s" % (fyd_art.d20(diceresult))
    answers = {'y': 'archer_story.part_2d'}
    return s, art, answers


def part_1cb():
    s = """
The guard puts the handcuffs on you and walks you out of the room.
Instead of taking you the way the other prisoners went he takes you 
the opposite way.
You begin to hear some talking so you think that now is the time to
 kill him.
With your wrists still in handcuffs you dislocate both your thumbs 
and slip your hands through the handcuffs.
You drop your handcuffs and the guard walking you looks down at them, 
you pull your dagger out and slice his throat.

    y) Continue? 
    """
    answers = {'y': 'archer_story.part_2d'}
    return s, fyd_art.archer(), answers


def part_2d():
    s = """
You walk the opposite way from the other prisoners trying to look for 
a way out.
You continue walking down the corridor until see a room with five guards
 inside.
The door is open and you peak inside, the five guards are talking and 
there is a large door behind them.
'That must be the way out' you think.
You look in your hand as the only weapon you have is a dagger.

    What do you do?
        a) Sneak up behind them and kill the guards sneakily.
        b) Run into the room and attack the guards.
    """
    answers = {'a': 'archer_story.part_2da', 'b': 'archer_story.part_2db'}
    return s, fyd_art.guards(), answers


def part_2da():
    s = """
You sneakily enter the room and you manage to slice two of the guards 
throats without making a sound.
The other tree guards then see you and start to run at you.
You're able to dodge a few blades and stab one of the guards.
But the other two guards were able to attack you as they impale you.
    %s""" % (fyd_art.you_died())
    answers = {}
    return s, fyd_art.archer(), answers


def part_2db():
    s = """
You run into the room and alert the guards.
All five of them turn around and pull out their swords.
They simultaneously swing at you, as you're unable to dodge out of the
 way you get chopped up.
    %s""" % (fyd_art.you_died())
    answers = {}
    return s, fyd_art.archer(), answers


def part_3a():
        s = """
Nice job, you've successfully made it out of the prison!
You have finished the archers story but you could've saved someone else!
You can play the archers story again to try and save them.
Are you ready to go back to the real world?

    y) I'm ready!
    """
        answers = {'y': 'quit'}
        return s, fyd_art.youwon(), answers


def part_3b():
    s = """
Nice job, you've successfully made it out of the prison!
You have finished the archers story as best as possible!
You were able to escape with the man that helped you.
Are you ready to go back to the real world?

    y) I'm ready!
    """
    answers = {'y': 'quit'}
    return s, fyd_art.youwon(), answers

def part_3c():
        s = """
Nice job, you've successfully made it out of the prison!
Unfortunately you have lost a man on the way out.
You can play the archers story again to try and save them.
Are you ready to go back to the real world?

    y) I'm ready!
    """
        answers = {'y': 'quit'}
        return s, fyd_art.youwon(), answers
