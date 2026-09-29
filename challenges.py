# ============================================
# CHALLENGE MODULE
# ============================================

from scoring import add_score


def academic_challenge(player):

    print("\n================================")
    print("       ACADEMIC CHALLENGE")
    print("================================")

    points = 0

    print("\nQuestion 1")
    print("What is the output of 5 + 3?")
    print("1. 6")
    print("2. 8")
    print("3. 10")

    answer = input("Enter your answer: ").strip()

    if answer == "2":
        print("Correct! +10 points")
        points = points + 10
    else:
        print("Incorrect! Correct answer is 2.")

    print("\nQuestion 2")
    print("Which keyword is used to define a function in Python?")
    print("1. function")
    print("2. define")
    print("3. def")

    answer = input("Enter your answer: ").strip()

    if answer == "3":
        print("Correct! +10 points")
        points = points + 10
    else:
        print("Incorrect! Correct answer is 3.")

    add_score(player, points)

    print("\nPoints earned:", points)
    print("Current score:", player["score"])


def innovation_challenge(player):

    print("\n================================")
    print("      INNOVATION CHALLENGE")
    print("================================")

    points = 0

    print("\nQuestion 1")
    print("Which symbol is used for a comment in Python?")
    print("1. //")
    print("2. #")
    print("3. /* */")

    answer = input("Enter your answer: ").strip()

    if answer == "2":
        print("Correct! +10 points")
        points = points + 10
    else:
        print("Incorrect! Correct answer is 2.")

    print("\nQuestion 2")
    print("Which loop is commonly used when the number of iterations is known?")
    print("1. for loop")
    print("2. while loop")
    print("3. if statement")

    answer = input("Enter your answer: ").strip()

    if answer == "1":
        print("Correct! +10 points")
        points = points + 10
    else:
        print("Incorrect! Correct answer is 1.")

    add_score(player, points)

    print("\nPoints earned:", points)
    print("Current score:", player["score"])


def library_challenge(player):

    print("\n================================")
    print("        LIBRARY CHALLENGE")
    print("================================")

    points = 0

    print("\nQuestion 1")
    print("Which data type is used to store text in Python?")
    print("1. int")
    print("2. str")
    print("3. float")

    answer = input("Enter your answer: ").strip()

    if answer == "2":
        print("Correct! +10 points")
        points = points + 10
    else:
        print("Incorrect! Correct answer is 2.")

    print("\nQuestion 2")
    print("Which function is used to display output in Python?")
    print("1. input()")
    print("2. print()")
    print("3. output()")

    answer = input("Enter your answer: ").strip()

    if answer == "2":
        print("Correct! +10 points")
        points = points + 10
    else:
        print("Incorrect! Correct answer is 2.")

    add_score(player, points)

    print("\nPoints earned:", points)
    print("Current score:", player["score"])


# ============================================
# TESTING CHALLENGE MODULE
# ============================================

if __name__ == "__main__":

    test_player = {
        "name": "Test Player",
        "score": 0,
        "locations_visited": []
    }

    print("Challenge module test")

    academic_challenge(test_player)

    print("\nFinal test score:", test_player["score"])