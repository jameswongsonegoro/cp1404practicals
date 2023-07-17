MINIMUM = 0


def main():
    passwords = get_password()
    print(passwords)


def get_password():
    password = input("Enter password: ")
    while len(password) <= MINIMUM:
        print("Invalid password")
        password = input("Enter password: ")
    passwords = len(password) * "*"
    return passwords


main()


