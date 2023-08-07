"""
CP1404/CP5632 Practical
Hexadecimal colour lookup
"""

COLOUR_CODES = {"Amethyst": "#9966cc", "Amber": "#ffbf00",
                "Aqua": "#00ffff", "Apricot": "#fbceb1",
                "Corn": "#fbec5d", "Coral": "#ff7f50",
                "Denim": "#1560bd", "Gray": "#bebebe",
                "Ginger": "#b06500", "Ebony": "#555d50"}

colour = input("Enter a colour name: ").title()
while colour != "":
    print(f"The code for {colour} is {COLOUR_CODES.get(colour)}")
    colour_name = input("Enter a colour name: ").title()