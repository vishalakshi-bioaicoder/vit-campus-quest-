# ============================================
# CAMPUS LOCATIONS MODULE
# ============================================

from challenges import academic_challenge, innovation_challenge, library_challenge


# ============================================
# ACADEMIC BLOCK
# ============================================

def academic_block(player):

    print("\n================================")
    print("        ACADEMIC BLOCK")
    print("================================")

    print("You entered the Academic Block.")
    print("You can find classrooms and laboratories here.")

    if "Academic Block" not in player["locations_visited"]:
        player["locations_visited"].append("Academic Block")

    print("\nLocation visited successfully!")

    academic_challenge(player)


# ============================================
# LIBRARY
# ============================================

def library(player):

    print("\n================================")
    print("            LIBRARY")
    print("================================")

    print("You entered the VIT Library.")
    print("The library is quiet and filled with books.")

    if "Library" not in player["locations_visited"]:
        player["locations_visited"].append("Library")

    print("\nYou found a Python programming book!")

    library_challenge(player)


# ============================================
# INNOVATION LAB
# ============================================

def innovation_lab(player):

    print("\n================================")
    print("        INNOVATION LAB")
    print("================================")

    print("You entered the Innovation Lab.")
    print("Students are working on different projects here.")

    if "Innovation Lab" not in player["locations_visited"]:
        player["locations_visited"].append("Innovation Lab")

    print("\nYou discovered a new project idea!")

    innovation_challenge(player)


# ============================================
# TESTING LOCATIONS MODULE
# ============================================

if __name__ == "__main__":

    test_player = {
        "name": "Test Player",
        "score": 0,
        "locations_visited": []
    }

    print("Locations module test")

    academic_block(test_player)
    library(test_player)
    innovation_lab(test_player)

    print("\nLocations visited:")
    print(test_player["locations_visited"])