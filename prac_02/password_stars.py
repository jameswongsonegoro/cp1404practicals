MINIMUM = 0


def main():
    password = input("Enter password: ")
    while len(password) <= MINIMUM:
        print("Invalid password")
        password = input("Enter password: ")
    passwords = len(password) * "*"
    print(passwords)


main()


