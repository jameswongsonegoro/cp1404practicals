"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
get sales
while sales >= 0
    calculate total_bonus
    get sales
display thank you message
"""

LOW_BONUS = 0.1
HIGH_BONUS = 0.15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        total_bonus = float(sales * LOW_BONUS)
    else:
        total_bonus = float(sales * HIGH_BONUS)
    print("Bonus = $", int(total_bonus), sep="")
    sales = float(input("Enter sales: $"))


