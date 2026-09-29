# ============================================
# SCORING MODULE
# ============================================


def add_score(player, points):

    player["score"] = player["score"] + points


def get_rank(score):

    if score >= 40:
        return "Campus Champion"

    elif score >= 30:
        return "Excellent Explorer"

    elif score >= 20:
        return "Smart Explorer"

    elif score >= 10:
        return "Campus Explorer"

    else:
        return "Beginner Explorer"
        # TESTING SCORING MODULE

if __name__ == "__main__":

    test_player = {
        "name": "Test Player",
        "score": 0,
        "locations_visited": []
    }

    print("Initial score:", test_player["score"])

    add_score(test_player, 10)

    print("After adding 10 points:", test_player["score"])
    print("Player rank:", get_rank(test_player["score"]))