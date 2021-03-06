import fyd_art
import dice_roll

def part_1():
    s = """
You wake up in a forest with the sun beaming down on your face 
partially blocked by your helmet.
You get up as your armour clunks around and look at your surroundings.
In front of you is an extinguished campfire, pieces of armour and 
weapons lying around you.
You look down near your feet and see your sword and shield.
You bend down and pick them up as you reflect the sunlight off of the 
sword as you admire it.
You see an emblem on your shield and try to recollect your thoughts, 
you start to remember.
This emblem is of the kingdom that you are knighted to.
You were off scouting the area with some fellow knights when it turned 
to night and decided to make camp.
But for the life of you, you can't seem to remember where your fellow 
knights went.
Suddenly you hear some rustling in a bush behind you, you spin around 
as fast as you can.

   What do you do?
      a) Start swinging at the bush aimlessly.
      b) Get in a defensive stance with your shield in front of you.
      c) Shout at the bush, ordering whatever it is to show itself.
    """

    answers = { 'a' : 'knight_story.part_1a', 'b': 'knight_story.part_1b', 'c': 'knight_story.part_1c'}
    return s, fyd_art.knight(), answers

def part_1a():
    s = """
You start slashing away at the bush until there is just the stem of the 
bush sticking out from the ground.
Behind the cut up bush you see a young boy in ragged clothes huddled 
together on the ground.
He seems to be asleep or dead but he isn’t breathing or moving and his 
skin looks very pale.

     What do you do?
        a) Slowly creep backwards, away from him.
        b) Poke him with your sword.
        c) Ask if he is ok.
    """
    answers = { 'a' : 'knight_story.part_1aa', 'b': 'knight_story.part_1ab', 'c': 'knight_story.part_1ac'}
    return s, fyd_art.knight(), answers


def part_1aa():
    diceresult = dice_roll.rolld20()
    if diceresult <11:
        s = """
You try to sneak away from the boy but as you do so you step on a 
sick and a loud ‘CRACK’ awakens him.
The boy gets up and you see his pale eyes and rotten skin much better 
now.
He begins to run at you and as he gets closer you whack your shield 
against him and he gets knocked down to the floor.
He lunges at you again and latches onto your foot and starts to tear
 away the armour on your leg, you kick him off and run away.
As you start making some distance from him you see your fellow soldiers 
limping towards you with their armour stripped from their body and 
their pale skin.
You manage to make it out of the forest but you have lost a few pieces 
of armour along the way.

    y) Continue?
        """

        art = "Unlucky roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = { 'y' : 'knight_story.part_2b'}

    else:
        s = """
You slowly creep backwards, away from the young boy and sneakily get 
out of view from him.
As you keep walking you hear some loud clanking, you hide behind a 
tree and see your fellow knights limping and wandering around.

    What do you do?
        a) Sneak away from them.
        b) Walk up to them.
            """

        art = "Woah nice roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = {'a': 'knight_story.part_1aaa', 'b': 'knight_story.part_1aab'}
    return s, art , answers


def part_1aaa():
    s = """
You decide not to disturb them as they aren't acting normal and you 
manage to make your way out of the forest safely.

    y) Continue?
    """
    answers = { 'y' : 'knight_story.part_2a'}
    return s, fyd_art.forest(), answers


def part_1aab():
    s = """
You start walking up to them and ask them ‘Hey what are you guys doing 
over here?’.
As you get closer to them you see that they have pale and rotten skin 
and when you look at their eyes they are completely pale.
You start to run away but they manage to grab a hold of you and tackle
 you to the ground.
They begin to take your armour off, you start swinging your sword at 
them and attempt to push them off of you with your shield but it is no
 use.
You feel pain all over your body as they sink their teeth into your 
flesh.
    
    %s""" % (fyd_art.you_died())
    answers = { 'a' : 'knight_story.part_1aab'}
    return s, fyd_art.zombie(), answers


def part_1ab():
    s = """
You poke the boy with your sword and he jumps up suddenly, his eyes are
 completely white and he looks undead.
He jumps at you but you already have your sword pointing at him and he
 jumps straight into your sword and gets impaled.
He goes limp and you push him off of your sword, you look around and 
try to think how and why there is a zombie out in the forest.
You decide to head out of the forest and after a short trek you make
 it out safely.

    y) Continue?
    """
    answers = { 'y' : 'knight_story.part_2a'}
    return s, fyd_art.zombie(), answers


def part_1ac():
    s = """
You whisper to the boy ‘Psst, are you alive?’, the boy doesn't move 
and you crouch down next to him and whisper into his ear.
‘Hellooo-.’ the boy jumps up from the ground and you are now face to
 face with his completely white eyes.
He jumps at your face but you don’t have time to react as you stumble 
to the ground and he knocks your helmet off and bites into your face.
    
    %s""" % (fyd_art.you_died())
    answers = { 'a' : 'knight_story.part_1ac'}
    return s, fyd_art.zombie(), answers


def part_1b():
    s = """
You get into a defensive stance and as you peek over the top of your 
shield you see the bush has stopped rustling.
Thinking whatever was in the bush is gone you begin to lower your 
shield.
When all of a sudden from the bush a young boy lunges at you and 
latches onto your shield.
He starts swinging at you with his sharp nails and you see that his 
eyes are completely white and his skin looks pale and rotten.
You attempt to shake him off your shield and he falls to the ground.

    What do you do?
        a) Attack him.
        b) Run away from him.
    """
    answers = { 'a' : 'knight_story.part_1ba', 'b': 'knight_story.part_1bb'}
    return s, fyd_art.zombie(), answers


def part_1ba():
    diceresult = dice_roll.rolld20()
    if diceresult <11:
        s = """
You swing your sword at the boy who is now on the ground but you lose 
your footing and slip on some leaves.
As you miss the boy the sword gets stuck in the ground and you fall 
onto your back.
The boy jumps back onto your shield and starts to swing at you, you 
start punching him until he falls to the ground.
You slowly get up and see that his head is destroyed with his brain 
exposed and maggots all inside of his head.
‘Is that a zombie?’, you pick up your sword and notice a trail that 
leads out of the forest, you start limping and following it.

    y) Continue?
        """

        art = "Unlucky roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = { 'y' : 'knight_story.part_2b'}
        return s, art, answers

    else:
        s = """
As he falls to the ground and attempts to get up you swing your sword 
down and cut off his head.
He goes limp and you try and catch your breath. ‘Was that...a zombie?’.
You look at your surroundings and see a trail that leads off out of the
 forest, you decide to follow it.

    y) Continue?
    """
        art = "Woah nice roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = { 'y' : 'knight_story.part_2a'}
        return s, art, answers


def part_1bb():
    diceresult = dice_roll.rolld20()
    if diceresult <11:
        s = """
The boy falls to the ground and you turn around and run as fast as you
 can.
You look back behind you and the boy is on all fours crawling towards
 you.
You turn your head back in the direction you are running towards and 
right in front of you are your fellow knights.
But they look like the young boy as they have pale, rotten skin and 
white eyes.
You try to get out of their way but they manage to latch onto you and
 pull you towards them.
You swing your sword at them and manage to cut a few of their arms off
 but as they claw at you they take some armour off of your body.
You try to push them away but they overwhelm you and you get swarmed.
        
        %s""" % (fyd_art.you_died())

        art = "Unlucky roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = {}
        return s, art, answers
    else:
        s = """
The boy falls to the ground and you turn around and run as fast as 
you can.
You look back behind you and the boy is on all fours crawling towards
 you.
You turn your head back in the direction you are running and right in
 front of you are your fellow knights.
But they look like the young boy as they have pale, rotten skin and 
white eyes.
You manage to move out of the way in time as they attempt to reach 
you with their sharp nails.
You continue running until you reach the outskirts of the forest.

    y) Continue?
    """
        art = "Woah nice roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = { 'y' : 'knight_story.part_2a'}
        return s, art, answers


def part_1c():
    s = """
You shout at the thing in the bush to show itself and the rustling stops.
You then hear the bushes all around you start to rustle and you can hear
 footsteps approaching slowly.
You start to look in every direction to see what's making the sound and
 you start to see your fellow knights approaching you.
But they’re acting weird, most of their armour is stripped from their
 body and they look...undead.

    What do you do?
        a) Attack him.
        b) Run away from him.
    """
    answers = { 'a' : 'knight_story.part_1ca', 'b': 'knight_story.part_1cb'}
    return s, fyd_art.zombie(), answers


def part_1ca():
    diceresult = dice_roll.rolld20()
    if diceresult <11:
        s = """
You attempt to kill them but you get outnumbered.
You swing your sword at them and manage to cut a few of their arms off
 but as they claw at you they take some armour off of your body.
You do manage to kill them but at the cost of some of your armour that
 they manage to tear off of you.
You hear the rustling in the bush once more but you decide that
 whatever is in there is bad news and you want to stay alive.
You wander off in the opposite direction of the rustling and manage 
to get out of the forest.

        y) Continue?
        """

        art = "Unlucky roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = { 'y' : 'knight_story.part_2b'}
        return s, art, answers
    else:
        s = """
As they slowly walk up to you, one by one you hack and slash at them
 until they are all dead.
You try to catch your breath and you hear the same rustling
 behind you.
You whip around and there is a young boy running on all fours at you
 and he also looks undead.
He jumps at you and you block him with your shield.
He bounces off your shield and you swing at him and with one clean
 cut you slice his head off.
You look at your surroundings to see if there's a way out of the forest.
You see a trail that you follow, it eventually leads you out of the
 forest.

    y) Continue?
        """
        art = "Woah nice roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = { 'y' : 'knight_story.part_2a'}
        return s, art, answers


def part_1cb():
    diceresult = dice_roll.rolld20()
    if diceresult <11:
        s = """
You attempt to run away from them but as you start to run you hear the
 rustling again.
Out runs on all fours a young boy who also looks undead.
He jumps at you and you get tackled to the floor.
As he pushed you to the floor your sword and shield flew out of your
 hands.
You are now pinned to the ground by the young boy and the other
 zombies are making their way towards you.
You are now zombie meat.

%s""" % ( fyd_art.you_died() )


        art = "Unlucky roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = {}
        return s, art, answers
    else:
        s = """
You decide not to fight them and you run the opposite direction.
You now find yourself outside of the forest.

    y) Continue?
        """
        art = "Woah nice roll!!\n\n\n%s" % (fyd_art.d20(diceresult))

        answers = { 'y' : 'knight_story.part_2a'}
        return s, art, answers


def part_2a():
        s = """
Nice job, you've successfully made it out of the forest unharmed!
You have finished the knights story as best as possible!
Are you ready to go back to the real world?
        
    y) I'm ready!
    """
        answers = {'y': 'quit'}
        return s, fyd_art.youwon(), answers


def part_2b():
        s = """
Nice job, you've made it out of the forest!
But you have either gotten injured or lost some armour along the way.
If you want to try and beat the knights story as best you can then play
 again.
Are you ready to go back to the real world?

    y) I'm ready!
    """
        answers = {'y': 'quit'}
        return s, fyd_art.youwon(), answers
