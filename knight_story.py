answer = input("WOULD YOU LIKE TO FULFIL YOUR DESTINY? (yes/no): ")
if answer.lower().strip() == "yes":

    answer = input("""
You wake up in a forest with the sun beaming down on your face partially being blocked by your helmet.
You get up as your armour clunks around and look at your surroundings.
In front of you is an extinguished campfire and pieces of armour and weapons lying around you.
You look down near your feet and see your sword and shield.
You bend down and pick them up as you reflect the sunlight off of the sword as you admire it.
You see an emblem on your shield and try to recollect your thoughts, you start to remember.
This emblem is of the kingdom that you are knighted to.
You were off scouting the area with some fellow knights when it turned to night and decided to make camp.
But for the life of you, you can't seem to remember where your fellow knights went.
Suddenly you hear some rustling in a bush behind you, you spin around as fast as you can.
    What do you do?
    a) Start swinging at the bush aimlessly.
    b) Get in a defensive stance with your shield in front of you.
    c) Shout at the bush, ordering whatever is inside to show itself.
""").lower().strip()

    if answer == "a":
        answer = input("""
You start slashing away at the bush until there is just the stem of the bush sticking out from the ground.
Behind the cut up bush you see a young boy in ragged clothes huddled together on the ground.
He seems to be asleep or dead but he isn’t breathing or moving and his skin looks very pale.
    What do you do?
    a) Slowly creep backwards, away from him.
    b) Poke him with your sword.
    c) Ask if he is ok.
""")
        if answer == "a":
            print("")

    elif answer == "b":
        answer = input("""
You get into a defensive stance and as you peek over the top of your shield you see the bush has stopped rustling.
Thinking whatever was in the bush is gone you begin to lower your shield.
When all of a sudden from the bush a young boy lunges at you and latches onto your shield.
He starts swinging at you with his sharp nails and you see that his eyes are completely white and his skin looks pale and rotten.
You attempt to shake him off your shield and he falls to the ground.
    What do you do?
""")

    elif answer == "c":
        answer = input("""
You shout at the thing in the bush to show itself and the rustling stops.
You then hear the bushes all around you start to rustle and you can hear footsteps approaching slowly.
You start to look in every direction to see what's making the sound and you start to see your fellow knights approaching you.
But they’re acting weird, most of their armour is stripped from their body and they look….undead.
    What do you do?
""")

else:
    print("Chicken!")
