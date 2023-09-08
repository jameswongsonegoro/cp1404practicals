"""
CP1404/CP5632 Practical
Quick pick program
"""

import random

NUMBERS_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick picks program"""
    chosen_number = int(input("How many quick picks? "))
    while chosen_number < 0:
        print("Invalid number")
        chosen_number = int(input("How many quick picks? "))

    for i in range(chosen_number):
        quick_pick = []
        for j in range(NUMBERS_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()
