MINIMUM = 0


def main():
    passwords = get_password()
    print(passwords)


def get_password():
    password = input("Enter password: ")
    while len(password) <= MINIMUM:
        print("Invalid password")
        password = input("Enter password: ")
    passwords = calculate_asterisks(password)
    return passwords


def calculate_asterisks(password):
    passwords = len(password) * "*"
    return passwords


main()


