"""Password check with functions"""

MINIMUM = 0


def main():
    """Changing the password output from characters to asterisks"""
    passwords = get_password()
    print(passwords)


def get_password():
    """Get the user input"""
    password = input("Enter password: ")
    while len(password) <= MINIMUM:
        print("Invalid password")
        password = input("Enter password: ")
    passwords = calculate_asterisks(password)
    return passwords


def calculate_asterisks(password):
    """Calculate the length of asterisks"""
    passwords = len(password) * "*"
    return passwords


main()


