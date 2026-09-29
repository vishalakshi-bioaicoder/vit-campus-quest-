# ===========# ============================================
# PLAYER MODULE
# ============================================

def create_player():

    name = input("Enter your name: ").strip()

    while name == "":
        print("Name cannot be empty.")
        name = input("Please enter your name: ").strip()

    player = {
        "name": name,
        "score": 0,
        "locations_visited": []
    }

    return player


def display_player_info(player):

    print("\n================================")
    print("        PLAYER PROFILE")
    print("================================")

    print("Name:", player["name"])
    print("Score:", player["score"])
    print("Locations visited:", len(player["locations_visited"]))


# TESTING PLAYER MODULE
if __name__ == "__main__":

    print("Player module test")

    player = create_player()

    print("\nPlayer created successfully!")

    display_player_info(player)