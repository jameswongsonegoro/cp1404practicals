"""Scores"""

import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
HIGH_SCORE = 90
LOW_SCORE = 50


def main():
    """Determine what type of score the user gets"""
    score = float(input("Enter score: "))
    message = determine_score(score)
    print(message)
    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(random_score)


def determine_score(score):
    """Determine the user's score"""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        message = "Invalid score"
    elif score >= HIGH_SCORE:
        message = "Excellent"
    elif score >= LOW_SCORE:
        message = "Passable"
    else:
        message = "Bad"
    return message


main()
