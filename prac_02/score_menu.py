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
            score = int(input("Your score: "))
            while score < 0 or score > 100:
                print("Invalid score")
                score = int(input("Your score: "))
            print(MENU)
            choice = input(">>> ").upper()
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
            print(MENU)
            choice = input(">>> ").upper()
        elif choice == "S":
            for i in range(int(score)):
                print("*", end=" ")
            print()
            print(MENU)
            choice = input(">>> ").upper()
        else:
            print("Invalid choice")
            print(MENU)
            choice = input(">>> ").upper()
    print("Farewell")


main()
