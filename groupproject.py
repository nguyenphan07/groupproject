"""
    group_project.py
    Jack    Nguyen  Daniel
    group 5 project about choose your own journey game
"""
#System import
from random import randint

#Global Variable
global NAME
NAME: str = input("Please enter your character's name: ") # Allow the player to name their character
print(f"Welcome {NAME} to the game!")

#Functions

def validation_check(choice: str, possibility: list[str]) -> str:
    """ Checks if user's input is eligible"""
    while not choice in possibility: # Activates if user inputs an ineligible choice, looping until user input a possible choice
        choice = input("Not an option, please try again: ")
    return choice # The function returns a possible choice (passed validation check)



def random_event(strength_random: int) -> tuple:
    """Adding random events in dark forest"""
    treasure: dict[str, int] ={     # Treasure is a dictionary with keys as items and value as strength points gained from obtaining the treasure
        "sword": 10,
        "shield": 5,
        "bow & arrows": 3
    }
    treasure_order: list[str] = ["sword", "shield", "bow & arrows"] # to easily organize the treasure in the dictionary
    monster: dict[str, int] ={
        "wolf": 10,
        "piranha plant": 15,
        "bear": 20
    }
    monster_order: list[str] = ["wolf", "piranha plant", "bear"] # to easily organize the monster in the dictionary

    monster_gain: dict [str, int] ={
        "wolf": 4,
        "piranha plant": 8,
        "bear": 12
    } # to give players strength points as rewards when defeating a monster
    i = randint(1,100) # Use to generate probability, (30% that a treasure will be found, 70% to encounter a random monster)
    if i <= 30: # 30% (gets treasure)
        i = randint(0,len(treasure_order) - 1) # Now this variable is used to randomly determine the treasure the player got
        print(f"You found a treasure!. it was a {treasure_order[i]}.\nYou gained {treasure[treasure_order[i]]} strength points!. You now have {strength_random + treasure[treasure_order[i]]} total.")
        strength_random += treasure[treasure_order[i]]
    else: # 70% (faces monster)

        i = randint(0,len(monster_order) - 1)
        print(f"A monster appeared! You are facing a {monster_order[i]}\n you need at least {monster[monster_order[i]]} strength points to beat it, you currently have {strength_random} points total.")
        print("Fight it?\n1. Fight\n2. Run")
        decision: str = input()
        possibility = ["1", "2"]
        decision = validation_check(decision, possibility)


        if decision == "1" and strength_random >= monster[monster_order[i]]: # Player choose to fight and has enough or more points to defeat the monster
            print(f"You have defeated the {monster_order[i]}! You have gained {monster_gain[monster_order[i]]} strength points from successfully defeating the monster.")
            strength_random += monster_gain[monster_order[i]]
            print(f"You now have {strength_random} strength points total.")


        elif decision == "2": #Player choose to run
            print("You ran away successfully. What an inconvenience!")


        else: #Player choose to fight but does not have enough strength points
            print(f"You have been slain by the {monster_order[i]}.\nGAME OVER!")
            print("1. Restart the chapter\n2. Exit the game")
            decision = input("Type '1' or '2'")
            decision = validation_check(decision, possibility)
            if decision == "1": # Restart
                return "restart", strength_random
            else: # Exit
                return "exit", strength_random
    return "alive", strength_random


def dark_forest() -> str | None:
    """Function to run dark forest chapter"""
    while True: # A loop, intention is when the player loses and wishes to restart, the loop will be activated
        starting_strength: int = 10 # stored so when player restarts, their strength is reset
        strength: int = starting_strength
        print("+-----------------------------------------------------------------+")
        print("You wake up in a dark forest. As you navigate, you notice 2 distinct paths to follow: \n1. A dim light illuminating at a distance \n2. A dark path leading deeper into the forest.")
        decision: str = input("What should you do? Type '1' or '2': ")
        two_possibility: list[str] = ["1", "2"] # Created a list of 2 possible choices that the user can input
        decision = validation_check(decision, two_possibility) #validate check user's input


        print("+-----------------------------------------------------------------+")
        if decision == "1": # Follow the light
            print("You found a cabin, though it seems like no one is inside.\n1. Go in the house \n2. Search around for items.")
            decision = input("What should you do? Type '1' or '2': ")
            decision = validation_check(decision, two_possibility)
            print("+-----------------------------------------------------------------+")


            if decision == "1": #Go inside the house
                print("The door opens on its own. \n\"Were you not taught to not enter other's property without consent?\" A voice comes inside the house.")
                print("Upon you, a witch appears. \"Oh you must be new here. You see, this is no ordinary forest.\n This whole forest is an entity, hungrily sucking living beings from different dimensions to feel fulfilled.\"")
                print("\"If you want to escape. You must find the dungeon hidden somewhere in the center of the forest.\n Because I pity you, here are some items that can help you\"")
                strength += 3
                print(f"You gained 3 strength points! Now you have {strength} total.")


            else: # Search around for items
                print("You found nothing, but a piece of paper that might explain why you're here. Read it?\n1. Yes\n2. No")
                decision = input("Type '1' or '2'")
                print("+-----------------------------------------------------------------+")
                decision = validation_check(decision, two_possibility)
                if decision == "1": # Read the note
                    print("\"What a nuisance! This forest has been sucking creatures from all over the places. Monsters, humans, animals, nothing is safe.\n I wish the dungeon of the forest is upon me right now! So I can escape this wicked place.")
            print("You left the cabin. Following a path that seems to be leading to somewhere...")



        else: #Follow the dark path
            print("As you move forward. The path eventually branches out. You notice two paths\n1. A straight path\n2. A wavy path")
            decision = input("Which path should you take? Type '1' or '2': ")
            print("+-----------------------------------------------------------------+")
            decision = validation_check(decision, two_possibility)


            if decision == "1": # Follow the straight path
                print("You found a skeleton, full of gears. You decided to take it to your advantage\n As you take off its gears, you noticed a diary. Ready it?\n1. Yes\n2. No")
                decision = input("Type '1' or '2': ")
                print("+-----------------------------------------------------------------+")
                decision = validation_check(decision, two_possibility)


                if decision == "1": # Read the diary
                    print("\"Oh I wish what that witch said was true. I've been going everywhere to find the dungeon to escape.\n Guess there is no luck for me. I hope I can make it out. This forest sucked me and other horrible creatures in. I wonder what is up with it...")
                strength += 5
                print(f"You have successfully acquired new gears. Now you have {strength} strength points total.")
                print("You kept moving forward, making turns based on your intuition...")

                
            else: #Follow the wavy path
                print("The path gets darker and darker. Suddenly, you don't know where you are anymore. You are lost.\nGAME OVER!")
                print("Do you want to:\n1. Restart the chapter\n2. Exit the game")
                decision = input("Type '1' or '2': ")
                print("+-----------------------------------------------------------------+")
                decision = validation_check(decision, two_possibility)
                if decision == "1":
                    strength = starting_strength
                    continue
                else:
                    return #end the function while returning nothing
        i = 1
        while i <= 3: # intended 3 randomized events
            print("+-----------------------------------------------------------------+")
            print("continue? press '1'")
            one_possibility = ['1']
            decision = input()
            decision = validation_check(decision, one_possibility)
            status, strength = random_event(strength)
            if status == "restart":
                break #stop the random event loop
            elif status == "exit":
                break #stop the random event loop
            else:
                i += 1
        if status == "restart": #Restarts the chapter
            strength = starting_strength
            continue
        elif status == "exit": #Exit the chapter
            return
        print("You finally found the dungeon hidden inside the forest. Wondering what's waiting for you... Chapter 1 complete!")
        return "complete"


### DUNGEON CHAPTER OVERALL (JACK)###
# Should we have impact decisions that carry through our different zones?
# One correct path 
# Daniel has exit message in his code

### IDEAS FOR THE DUNGEON ###
# DIE Dungeon, Dungeon of death -> "Time to Die" 
# Dice choices - Six Sided, D20, even/odd
# Fully random to get through? just an RNG check
# Play a dice game (Yatzee, craps, gambling) win to get past

## Dice used for randomness
## Other lists and dictionaries used 
def dungeon():
    "Runs the dungeon portion of the game."
    while True:
        # d6 = random.randint(1, 6) #WIP
        # d20 = random.randint(1, 20)
        # cards: dict[str, int] = { # Name and value of cards
        #     "Ace": 1,
        #     "Two": 2,
        #     "Three": 3,
        #     "Four": 4,
        #     "Five": 5,
        #     "Six": 6,
        #     "Seven": 7,
        #     "Eight": 8,
        #     "Nine": 9,
        #     "Ten": 10,
        #     "Jack": 10,
        #     "Queen": 10,
        #     "King": 10,
        #     "Ace High": 11
        # } 

        # print("PLACEHOLDER INTRO")
        print(f"{NAME}, You are in the Dungeon of ... Die\n")
        print("")

        # player_choice = int(input()) #WIP
        # if player_choice == 1:
        #     print("Good choice, Now choose a die to work with:\n1) 20 Sided Die\n2) Six Sided Die")
        # elif player_choice == 2:
        #     print("")
        # else:
        #     print("Invalid input, try again")
        #     player_choice = int(input())

        print("Let's play a game called BlackJack. I assume you know the rules.")
        player = randint(2, 11) #Get a starting value for the player
        dealer = randint(17, 22) #Get a value of the dealer
        print(f" Your current value is {player}")

        print("'Hit' or 'Stand'?")

        bet: str = input("Press '1' for Hit, press '2' for Stand: ")
        two_possibility: list[str] = ["1", "2"]
        bet = validation_check(bet, two_possibility)
        while bet == "1": #Hit
            draw = randint(2, 11) #Draw a random card
            player += draw

            print(f"You are on {player}")
            
            if player > 21:
                print("You Busted! Game Over!")
                break #break the 'hit' loop because player has lost
            bet = input("Continue? Press '1' for Hit, press '2' for Stand: ")
            bet = validation_check(bet, two_possibility)


        if player <= 21:
            print(f"Dealer's total:, {dealer}")

            if dealer > 21:
                print("Dealer busts! You win!")
                return "complete" #End the function while returning "complete"
            elif player > dealer:
                print("You win!")
                return "complete" #End the function while returning "complete"
            elif player < dealer:
                print("Dealer wins!")
            else:
                print("Tie! The house always wins!")
        print("Do you want to:\n1. Restart the chapter\n2. Exit the game")
        decision = input("Type '1' or '2': ")
        print("+-----------------------------------------------------------------+")
        decision = validation_check(decision, two_possibility)
        if decision == "1": 
            continue
        if decision == "2":
            break
        return #End the function while returning nothing

"""Daniel's maze section """
def maze_section(): # https://learn.zybooks.com/zybook/NORMANDALECSCI1101RunningenFall2026/chapter/13/section/1
    """
    Runs the maze portion of the adventure game.
    The player must make choices to find the exit.
    """
    while True:
        print("\n=== THE ANCIENT MAZE ===")
        print("You leave the dungeon and enter a stone maze.")
        print("Find the exit before you get lost!\n")

        correct_paths: int = 0

        # Choice 1
        while True:
            choice1: str = input(
                "You reach your first intersection.\n"
                "Choose LEFT, RIGHT, or FORWARD: ").lower() #converts user input to lower case to prevent discrepancies
            if choice1 in ["left", "right", "forward"]:
                break # https://learn.zybooks.com/zybook/NORMANDALECSCI1101RunningenFall2026/chapter/11/section/11 
                    # break is used to stop the loop if user enters correct input
            print("Invalid choice. Please type LEFT, RIGHT, or FORWARD.")

        if choice1 == "left":
            print("You find strange footprints.")
            correct_paths += 1
        elif choice1 == "right":
            print("You walk into a dead end and must backtrack.")
        else:
            print("You discover a torch lighting the way.")
            correct_paths += 1

        print()

        # Choice 2
        while True:
            choice2: str = input(
                "A stone door blocks your path.\n"
                "Do you CLIMB over it, PUSH it open, or SEARCH for another way? "
            ).lower()

            if choice2 in ["climb", "push", "search"]:
                break
            print("Invalid choice. Please type CLIMB, PUSH, or SEARCH.")

        if choice2 == "search":
            print("You find a secret passage.")
            correct_paths += 1
        elif choice2 == "push":
            print("The door opens with great effort.")
        else:
            print("You slip but recover safely.")

        print()

        # Choice 3
        while True:
            choice3: str = input(
                "At the center of the maze is a glowing rune.\n"
                "Do you TOUCH it, IGNORE it, or READ it? "
            ).lower()

            if choice3 in ["touch", "ignore", "read"]:
                break 
            print("Invalid choice. Please type TOUCH, IGNORE, or READ.")

        if choice3 == "read":
            print("The rune reveals the way out!")
            correct_paths += 1
        elif choice3 == "touch":
            print("The maze shifts around you.")
        else:
            print("Nothing happens.")

        print()

        # Ending based on previous choices
        if correct_paths >= 3:
            print("Perfect navigation!")
            print("You quickly locate the maze exit and escape safely.")
            return "complete"
        elif correct_paths == 2:
            print("After some wandering, you eventually find the exit.")
            return "complete"
        else:
            print("You become lost and are trapped in the maze forever.")
            print("Do you want to:\n1. Restart the chapter\n2. Exit the game")
            decision = input("Type '1' or '2': ")
            two_possibility: list[str] = ["1", "2"]
            print("+-----------------------------------------------------------------+")
            decision = validation_check(decision, two_possibility)
            if decision == "1":
                continue
            else:
                return #end the function while returning nothing



if dark_forest() == "complete":
    if dungeon() == "complete":
        if maze_section() == "complete":
            print("== END OF MAZE ==")
            print(f"Congrats {NAME}, you have beat the game!")



