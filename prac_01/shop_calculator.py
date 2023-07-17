"""
get number of item
while number of item < 0
    display invalid message
    get number of item
else
    get price
    if total price > 100
        calculate discount price
        display discount price

"""


number_item = int(input("Number of items: "))
total_price = 0
while number_item < 0:
    print("Invalid number of items")
    number_item = int(input("Number of items: "))

for i in range(number_item):
    price = float(input("Price of item: "))
    total_price += price
if total_price > 100:
    discount_price = float(total_price - (total_price * 0.1))
    print(f"Total price for {number_item} is ${discount_price:.2f}")
