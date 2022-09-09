# Ethan Hollander Year 11 CompositeDeviceSci General

#
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣷⣶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀. 　　　。　　　　•　 　ﾟ　　。 　　.
# ⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⠁⣰⣿⣿⣿⡿⠿⠻⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠏⠀⣴⣿⣿⣿⠉⠀⠀⠀⠀⠀⠈⢻⣿⣿⣇⠀⠀⠀　　　.　　　 　　.　　　　　。　　 。　.
# ⠀⠀⠀⠀⢀⣠⣼⣿⣿⡏⠀⢠⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡀⠀
# ⠀⠀⠀⣰⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀.　　 。　　　• . 　　 • 　　　　•
# ⠀⠀⢰⣿⣿⡿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⠁⠀ﾟ Red was not An Impostor.　 ඞ。　.
# ⠀⠀⣿⣿⣿⠁⣿⣿⣿⡇⠀⠀⠻⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⠃⠀　'　　 1 Impostor remains 　 　　。⠀⠀
# ⠀⢰⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
# ⠀⢸⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠉⢉⣿⣿⠀⠀⠀⠀⠀⠀　　ﾟ　　　.　　　. 　　　　.　 .
# ⠀⢸⣿⣿⣇⠀⣿⣿⣿⠀⠀⠀⠀⠀⢀⣤⣤⣤⡀⠀⠀⢸⣿⣿⣿⣷⣦⠀⠀⠀
# ⠀⠀⢻⣿⣿⣶⣿⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠉⠉⠻⣿⣿⡇⠀⠀
# ⠀⠀⠀⠛⠿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠈⠹⣿⣿⣇⣀⠀⣠⣾⣿⣿⡇⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣦⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠛⠋⠉⠉⠁⠀
#


# importing useful things
import time
import random
import sys

# this section is for variables
state = {
    "player_name": "",
    "room": "start",
    "key": False,
    "looked_for_key": False,
    "light": False,
    "easter_egg": False,
    "phealth": 10,
    "ehealth": 10,
}

###################################################
# This section is where we define all our functions
# Pause break making a clean refresh on the screen
def pause():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")


# start dungeon welcome text
def start_dungeon():
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Welcome to, 'Escape the Dungeon!'")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    time.sleep(2)
    # Adding players name into the game
    print("Before you start, what's your name?")
    player_name = input("> ")
    state["player_name"] = player_name
    print("Thanks, " + player_name + ", and enjoy the game!")
    time.sleep(2)
    pause()


# quitting the game
def quit():
    print("Victor is so sad you have quit the game.")
    state["room"] = "quit"


# enter random junk
def victor():
    print("Victor says you can't do that :(")
    time.sleep(1.5)


# dying
def die():
    print("You die")
    time.sleep(1)
    print("quite sad, isn't it")
    time.sleep(1.5)
    print("Actions available: restart, quit")
    action = input("> ")
    if action == "restart":
        print("Restarting")
        time.sleep(1)
        print(".")
        time.sleep(0.7)
        print("..")
        time.sleep(0.7)
        print("...")
        time.sleep(0.7)
        print("Done!")
        time.sleep(1)
        state["key"] = False
        state["looked_for_key"] = False
        state["light"] = False
        state["phealth"] = 10
        state["ehealth"] = 10
        state["easter_egg"] = True
        pause()
        state["room"] = "start"
    elif action == "quit":
        quit()
    else:
        victor()


###################################################
# ROOMS
# Creating the start room
def start_room():
    print("You are standing in the entrance to the dungeon. There is no exit.")
    time.sleep(2)
    print("Actions available: forward, look")
    action = input("> ")
    # detecting what input you give it
    if action == "look":
        print("The room is dusty.")
        time.sleep(1)
        print("You hear a sound behind you.")
        time.sleep(1)
        print("A scrubby rat crawled to the leaky pipe,")
        time.sleep(1.5)
        print("It scowers the pipes...")
        time.sleep(2)
    # moving forwards
    elif action == "forward":
        pause()
        state["room"] = "middle"
    # quitting
    elif action == "quit":
        quit()
    # anything else
    else:
        victor()


###########################
# Creating the 2nd room
def middle_room():
    # making the script if theres no light on
    if state["light"] is False:
        print("You are in a room of the dungeon.")
        time.sleep(1)
        print("It's too dark to see.")
        time.sleep(1)
        print("The room looks endless with the haze.")
        time.sleep(2)
        print("You feel around the wall and find what seems to be a light switch")
        time.sleep(3)
    else:
        print("There is a door at the end of the long hallway")
        time.sleep(2)

    # checking if you have the key or have looked for the key.
    if state["key"]:
        print("Actions available: forward, backward")
    elif state["looked_for_key"]:
        print("Actions available: backward, look, pickup")
    elif state["light"]:
        print("Actions available: backward, look")
    else:
        print("Actions available: backward, inspect switch")
    action = input("> ")

    # Moving rooms
    if action == "inspect switch":
        # turning the light on // unlocks forwards in the dungeon
        print("You flick on the light switch.")
        time.sleep(1.5)
        print("The lights flicker on with an eerie sound.")
        state["light"] = True
        time.sleep(2)
    elif action == "forward":
        # checking if you have the key to escape
        if state["key"]:
            pause()
            state["room"] = "room3"
        else:
            print("The door is locked.")
    # quitting the game
    elif action == "quit":
        quit()
    # moving backwards
    elif action == "backward":
        pause()
        state["room"] = "start"
    # looking in the room
    elif action == "look":
        print("You spot a key on the floor.")
        time.sleep(1)
        state["looked_for_key"] = True
    # picking up the key
    if state["looked_for_key"] is True:
        if action == "pickup":
            print("You picked up the key!")
            time.sleep(1)
            state["key"] = True


########################
# Creating the fake room / transition room
def room3():
    print("This room looks identical to the last...")
    time.sleep(1.5)
    print("The endless fog seeping into the distance.")
    time.sleep(1.5)
    print("Actions available: backward, look, venture")
    action = input("> ")
    # detecting the action input
    if action == "look":
        print("You feel around the wall.")
        time.sleep(1)
        print("Not to your surprise the switch is in the same spot")
        time.sleep(2)
        print("You flick on the switch, nothing happens...")
        time.sleep(1.7)
        print(".")
        time.sleep(0.7)
        print(".")
        time.sleep(0.7)
        print(".")
        time.sleep(0.7)
        print("WHOMP")
        time.sleep(1)
        print("The ground opens beneath you..")
        time.sleep(1.5)
        pause()
        state["room"] = "room4"
    elif action == "backward":
        state["room"] = "middle"
    elif action == "venture":
        print("You wander into the darkness, not afraid")
        time.sleep(1.5)
        print("You feel all four walls, no doors on any of them")
        time.sleep(2)
    elif action == "quit":
        quit()
    else:
        victor()


##############################
# creating room 4 (the rat room)
def room4():
    print("You fall into a puddle of a sticky liquid.")
    time.sleep(2)
    print("While getting out of the goo, you hear heavy breathing from across the room")
    time.sleep(3)
    print("You go over to the light switch on the wall and turn it on.")
    time.sleep(2.7)
    print("'Ahhh!' you scream")
    time.sleep(1.3)
    print("In the distance where you heard the breathing was a 7-foot tall mole rat")
    time.sleep(3)
    print("Actions available: look, cry")
    action = input("> ")
    # detecting actions
    if action == "cry":
        print("You cry out for help")
        time.sleep(1)
        print("'AHH HELP ME!!'")
        time.sleep(1)
        print("You see the huge monster's eyes open, staring at you")
        time.sleep(2.7)
        print("It walks over to you and sniffs you")
        time.sleep(2)
        print("You try to stay as still as you can, shaking")
        time.sleep(2.2)
        print("It opens it's mouth and swallows you whole")
        time.sleep(2)
        die()
    elif action == "look":
        print("You notice theres no door at the end")
        time.sleep(2)
        print("There's a vent on the wall")
        time.sleep(1.5)
        print("But it's too high to reach")
        time.sleep(1.5)
        print("You move near the beast to sneak a peak behind it")
        time.sleep(2.7)
        print("Theres a ladder behind it's glutes")
        time.sleep(2)
        print("Try to slide past the freak, but you feel something")
        time.sleep(3)
        print("You notice it's whiskers moving around")
        time.sleep(2)
        print("Your body sinks into the wall and your heart starts to race")
        time.sleep(3)
        print("The mole rat moves away from you, now awake")
        time.sleep(2.3)
        print("It looks at you and does what you think is a smile")
        time.sleep(2.6)
        print("'GREETINGS FOOL, WELCOME TO MY DOMAIN!'")
        time.sleep(2)
        print("You were shocked it spoke! Nonetheless English")
        time.sleep(2.4)
        print("'uhh, hello?'")
        time.sleep(1.5)
        print("'I AM VICTOR, THE CONQUEROR'")
        time.sleep(1.5)
        print("'AND I CHALLENGE YOU TO A DANCE FIGHT!'")
        time.sleep(2)
        # Making player name UPPERCASE
        uppername = state["player_name"].upper()
        print("'AND IF YOU WANT TO SURVIVE, " + uppername + ", YOU BETTER WIN!'")
        time.sleep(3)
        pause()
        state["room"] = "roombb"
    elif action == "quit":
        quit()
    else:
        victor()


######################
# Boss fight scene
def roombb():
    ehealth = state["ehealth"]
    exitfight = False
    while exitfight != True:
        bossb = random.randint(1, 10)
        # Enemy looses points
        if bossb > 4:
            # telling the player the HPs
            print(state["player_name"] + "'s HP: " + str(state["phealth"]))
            print("Enemy's HP: " + str(state["ehealth"]))
            time.sleep(2)
            # Specific random events
            if bossb == 4:
                print("+ You hit the woah, propelling the monster against the wall.")
            elif bossb == 5:
                print("+ You dabbed on them haters, causing a catastrophic shock wave")
            elif bossb == 6:
                print("+ You did a TikTok dance, stunning the enemy's eyes")
            elif bossb == 7:
                print("+ You moonwalked all into the enemy's space")
            elif bossb == 8:
                print("+ You did what you thought was a Fortnite emote, it looked more like a goat falling over")
            elif bossb == 9:
                print("+ You hit the steps correctly")
            elif bossb == 10:
                print("+ You did the stanky leg")
            # Actual health change
            state["ehealth"] = state["ehealth"] - 1
            time.sleep(2)
        # You loose health
        else:
            print(state["player_name"] + "'s HP: " + str(state["phealth"]))
            print("Enemy's HP: " + str(state["ehealth"]))
            time.sleep(2)
            # Specific dance move atacks
            if bossb == 1:
                print("- The mole rat does a head spin, making you dizzy.")
            elif bossb == 2:
                print("- 'It's Molein' Time', Victor Moled all over you.")
            else:
                print("- Victor did the robot, causing sparks from the lights")
            # Actual health change
            state["phealth"] = state["phealth"] - 1
            time.sleep(2)
        # leaving the loop
        # cant find a better way so this is what i did
        if state["phealth"] <= 0:
            exitfight = True
        elif state["ehealth"] <= 0:
            exitfight = True
    # checking if you lost or won
    if state["phealth"] <= 0:
        die()
    elif state["ehealth"] <= 0:
        pause()
        state["room"] = "room5"


######################
def room5():
    print("The mole rat fell to the floor with a massive thump")
    time.sleep(2.5)
    # Making player name UPPERCASE
    uppername = state["player_name"].upper()
    print("'OKAY, " + uppername + ", YOU WIN! GG'")
    time.sleep(2)
    print("Victor's eyes close into a deep sleep")
    time.sleep(1.8)
    print("You grab the ladder and move it in front of the vent")
    time.sleep(2.5)
    print("You climb up the ladder, into the vent")
    time.sleep(2)
    # easter egg for being sussy in the vent
    if state["easter_egg"] == True:
        print("")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("Easter Egg Unlocked:")
        print("YOU SUSSY BAKA, GET OUT OF THE VENTS")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("")
        time.sleep(4)
    print("The vent leads to a trap door in the roof")
    time.sleep(1.7)
    print("You open the hatch, and it leads to the surface!")
    time.sleep(2)
    state["room"] = "exit"


######################
# this is the exit_dungeon function. It runs at the end of the game
def exit_dungeon():
    pause()
    print("You managed to escape the dungeon in one piece.")
    time.sleep(3)
    print("Congratz, gg!")
    time.sleep(1.5)
    print("Thanks for playing!")
    time.sleep(1.5)
    print("'WHERE DO YOU THINK YOU'RE GOING?'")
    time.sleep(2)
    print("'what? i thought he died...'")
    time.sleep(1.8)
    print("'YOU THINK YOU'RE LEAVING?'")
    time.sleep(1.5)
    print("'PYTHON: Program shutting down in 10 seconds'")
    time.sleep(2)
    print("'WHAT?!'")
    time.sleep(1)
    print("'HEY SYSTEM, OVERRIDE! C'MON'")
    time.sleep(1.5)
    print("'PYTHON: System override requested. User input required'")
    time.sleep(2.5)
    print("Action's available: Override, Cancel")
    action = input("> ")
    if action == "Override":
        print("'PYTHON: Program shutting down in 5'")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Goodbye World!")
        sys.exit()
    elif action == "Cancel":
        print("'PYTHON: Program shutdown overriden'")
        time.sleep(1.5)
        # Making player name UPPERCASE
        uppername = state["player_name"].upper()
        print("'YOU REALLY ARE DUMB, " + uppername + ", AREN'T YOU'")
        time.sleep(2)
        print("You here a sound behind you")
        time.sleep(1)
        print("You turn around and see Victor standing in front of your nose")
        time.sleep(3)
        print("He looks down directly into your eyes")
        time.sleep(2)
        print("He sniffs, then gobbles you up whole")
        time.sleep(2)
        die()
    elif action == "quit":
        quit()
    else:
        victor()


#################################################
# THIS SECTION IS WHERE THE MAIN GAME CODE STARTS
start_dungeon()
while state["room"] != "quit":
    while state["room"] != "exit":
        if state["room"] == "start":
            start_room()
        elif state["room"] == "middle":
            middle_room()
        elif state["room"] == "room3":
            room3()
        elif state["room"] == "room4":
            room4()
        elif state["room"] == "roombb":
            roombb()
        elif state["room"] == "room5":
            room5()
    exit_dungeon()
