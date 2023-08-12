"""
CP1404 Practicals
Email to name dictionary
"""


def main():
    """Create dictionary emails to name."""
    email_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email, name in email_name.items():
        print(f"{name} ({email})")


def get_name(email):
    """Extract name from email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
