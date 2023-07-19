MENU = "(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit"


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


main()