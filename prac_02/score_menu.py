MENU = "(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit"
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
HIGH_SCORE = 90
LOW_SCORE = 50


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Your score: "))
            while score < 0 or score > 100:
                print("Invalid score")
                score = float(input("Your score: "))
            print(MENU)
        elif choice == "P":
            if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
                message = "Invalid score"
            elif score >= HIGH_SCORE:
                message = "Excellent"
            elif score >= LOW_SCORE:
                message = "Passable"
            else:
                message = "Bad"
            print(message)


main()
