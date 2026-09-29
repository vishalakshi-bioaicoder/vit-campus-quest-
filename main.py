# ============================================
# VIT CAMPUS QUEST
# MAIN GAME
# ============================================

from player import create_player
from locations import academic_block, library, innovation_lab
from scoring import get_rank


# ============================================
# GAME START
# ============================================

print("================================")
print("       VIT CAMPUS QUEST")
print("================================")

player = create_player()

print("\nWelcome,", player["name"] + "!")
print("Your campus adventure begins.")


# ============================================
# MAIN GAME LOOP
# ============================================

choice = ""

while choice != "4":

    print("\n================================")
    print("          CAMPUS MENU")
    print("================================")

    print("1. Academic Block")
    print("2. Library")
    print("3. Innovation Lab")
    print("4. Exit Game")

    choice = input("\nWhere do you want to go? ").strip()

    if choice == "1":

        academic_block(player)

    elif choice == "2":

        library(player)

    elif choice == "3":

        innovation_lab(player)

    elif choice == "4":

        print("\n================================")
        print("          GAME COMPLETE")
        print("================================")

        print("Thank you for playing,", player["name"])
        print("Locations visited:", len(player["locations_visited"]))
        print("Final score:", player["score"])
        print("Player rank:", get_rank(player["score"]))

        print("\nThanks for playing VIT Campus Quest!")

    else:

        print("\nInvalid choice!")
        print("Please enter 1, 2, 3, or 4.")