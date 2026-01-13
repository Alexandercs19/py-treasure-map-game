print('''
      ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/\n''')
print("Welcome to Treasure Island!")
print("Your mission is to find the Treasure!")
print("Your decisions will decide your fate.")
print("So, let's begin!\n")

# -------------------- PROLOGUE: Choose an item --------------------
print("Before you move, you spot 3 items on the sand:")
print("1) coin  2) rope  3) torch")
item = input("Pick one (coin/rope/torch): ").lower()

has_coin = False
has_rope = False
has_torch = False

if item == "coin":
    has_coin = True
    print("\nYou took the COIN. It has a tiny sun symbol.")
elif item == "rope":
    has_rope = True
    print("\nYou took the ROPE. It feels strong.")
elif item == "torch":
    has_torch = True
    print("\nYou took the TORCH. The flame is steady.")
else:
    print("\nYou didn't choose correctly and grab nothing.")

# -------------------- STAGE 1: Crossroad --------------------
cross_road = input("\nYou're at a crossroad. Type 'right' or 'left': ").lower()

if cross_road == "left":
    print("\nYou go LEFT. The path is quiet...")

    # -------------------- STAGE 2: Jungle Encounter --------------------
    print("\nA jungle fork appears:")
    print("- A cave entrance (dark)")
    print("- A hill trail (windy)")
    jungle = input("Type 'cave' or 'hill': ").lower()

    if jungle == "cave":
        print("\nYou enter the cave.")

        if has_torch == True:
            print("Your TORCH lights the way. You see symbols on the wall.")
            print("One symbol looks like a sun pointing EAST.")
        else:
            print("It's too dark. You step carefully...")

        cave_choice = input("Inside the cave you see two tunnels. Type 'left' or 'right': ").lower()

        if cave_choice == "left":
            print("\nYou choose the left tunnel.")

            if has_rope == True:
                print("A small gap appears, but your ROPE helps you climb safely.")
                print("You find a small note: 'Yellow is warmer than it looks.'")
            else:
                print("A small gap appears. You jump and barely make it.")
                print("You survive, but you feel tired.")

        elif cave_choice == "right":
            print("\nYou choose the right tunnel.")

            if has_torch == True:
                print("With the TORCH you spot sleeping bats and move quietly.")
                print("You find a scratched message: 'Help the wounded.'")
            else:
                print("You wake the bats. They swarm you.")
                print("GAME OVER 🦇")

        else:
            print("\nYou get lost in the cave.")
            print("GAME OVER 🕳️")

    elif jungle == "hill":
        print("\nYou climb the hill trail.")

        if has_coin == True:
            print("Your COIN shines in the sun and reveals a hidden arrow on a rock.")
            print("The arrow points toward a lake.")
        else:
            print("The wind is strong. You keep walking until you see a lake.")

    else:
        print("\nYou hesitate too long. A wild boar charges you.")
        print("GAME OVER 🐗")

    # -------------------- STAGE 3: Lake (more options) --------------------
    print("\nYou reach a lake.")
    print("You see 3 options:")
    print("- swim (fast but risky)")
    print("- wait (slow but safe)")
    print("- build (try to build a raft)")

    water_decision = input("Type 'swim', 'wait', or 'build': ").lower()

    if water_decision == "wait":
        print("\nYou wait... a small boat arrives.")
        print("The ferryman says: 'Patience is rare. Step in.'")

    elif water_decision == "swim":
        print("\nYou swim into cold water...")

        if has_torch == True:
            print("You lift the TORCH high. A shadow in the water backs away.")
            print("You reach the other side safely.")
        else:
            print("Something grabs your leg.")
            print("GAME OVER 🐊")

    elif water_decision == "build":
        print("\nYou try to build a raft.")

        if has_rope == True:
            print("With ROPE you tie logs together. The raft works!")
            print("You cross safely.")
        else:
            print("Without ROPE the raft falls apart.")
            print("GAME OVER 🪵")

    else:
        print("\nYou freeze and do nothing until night.")
        print("GAME OVER 🌙")

    # -------------------- STAGE 4: Stranger (more outcomes) --------------------
    print("\nOn the other side, a stranger is bleeding.")
    print("He says: 'Help me and I'll help you.'")
    stranger_decision = input("Type 'yes' or 'no': ").lower()

    has_key = False

    if stranger_decision == "yes":
        print("\nYou help the stranger.")
        print("He gives you a KEY and says: 'Choose yellow when the time comes.'")
        has_key = True
    elif stranger_decision == "no":
        print("\nYou ignore him.")
        print("He smiles: 'Then you will guess alone.'")
    else:
        print("\nYou say nothing. The stranger disappears.")

    # -------------------- STAGE 5: Door Hall (deeper + extra option) --------------------
    print("\nYou enter a hallway with doors: red, black, yellow, white, blue.")
    print("A plaque reads: 'Two doors punish. Two doors spare. One door rewards.'")

    if has_coin == True:
        print("Your COIN sun symbol matches a tiny sun scratch near the YELLOW door.")

    door_decision = input("Choose a door color: ").lower()

    if door_decision == "yellow":
        print("\nYou chose YELLOW. It opens smoothly.")

        # -------------------- STAGE 6: Final Room (two choices + key logic) --------------------
        print("\nA treasure chest sits on a pedestal.")
        print("Two buttons are on the pedestal: 'open' and 'inspect'.")
        final_action = input("Type 'open' or 'inspect': ").lower()

        if final_action == "inspect":
            print("\nYou inspect the chest and notice a trap needle.")

            if has_key == True and stranger_decision == "yes":
                print("You use the KEY to disable the trap.")
                print("You safely open the chest.")
                print("🎉 CONGRATULATIONS! YOU WON! 🎉")
            else:
                print("You try to disable the trap with your hands...")
                print("It activates.")
                print("GAME OVER ☠️")

        elif final_action == "open":
            print("\nYou try to open the chest immediately...")

            if (stranger_decision == "yes") or (has_coin == True):
                print("The chest opens! The treasure is yours.")
                print("🏆 BEST ENDING! YOU WIN! 🏆")
            else:
                print("A trap activates because you rushed.")
                print("GAME OVER ⚡")

        else:
            print("\nYou do nothing and the room locks behind you.")
            print("GAME OVER 🚪")

    elif door_decision == "red" or door_decision == "blue":
        if door_decision == "red":
            print("\nYou open RED. Flames burst out.")
            print("GAME OVER 🔥")
        else:
            print("\nYou open BLUE. Freezing air pushes you out.")
            print("BAD ENDING 😅")

    elif door_decision == "black" or door_decision == "white":
        if door_decision == "black":
            print("\nYou open BLACK. A pit opens under you.")
            print("GAME OVER 🕳️")
        else:
            print("\nYou open WHITE. It's safe, but empty.")
            print("You survive... but no treasure.")
            print("NEUTRAL ENDING 🙂")

    else:
        print("\nThat door doesn't exist.")
        print("GAME OVER 🚫")

elif cross_road == "right":
    print("\nYou go RIGHT... and step on a trap plate.")

    if has_rope == True:
        print("You throw your ROPE forward and stop yourself from falling.")
        print("You crawl back to safety.")
        print("You try again and choose LEFT next time...")
        print("GAME OVER (but you learned) 😅")
    else:
        print("Arrows shoot from the walls.")
        print("GAME OVER ☠️")

else:
    print("\nInvalid direction. GAME OVER.")




