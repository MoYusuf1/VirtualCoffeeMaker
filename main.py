import data

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

ESPRESSO_PRICE = 1.50
LATTE_PRICE = 2.50
CAPPUCCINO_PRICE = 3.0


def welcome_screen():
    print("Welcome to the Virtual Coffee Machine.")
    print("ESPRESSO - $1.50, LATTE - $2.50, CAPPUCCINO - $3.00")
    choice = input("\nWhat would you like? (lowercase only): ")
    return choice


def insert_coins():
    q = int(input("\nHow many quarters will you insert?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickles?: "))
    p = int(input("How many pennies?: "))

    payment = int(q * QUARTERS + d * DIMES + n * NICKLES + p * PENNIES)
    print(f"You paid ${payment}\n")
    return payment


def change(selection, payment):
    if selection == "espresso" and payment >= ESPRESSO_PRICE:
        extra = int(payment - ESPRESSO_PRICE)
        return extra
    elif selection == "latte" and payment >= LATTE_PRICE:
        extra = int(payment - ESPRESSO_PRICE)
        return extra
    elif selection == "cappuccino" and payment >= CAPPUCCINO_PRICE:
        extra = int(payment - LATTE_PRICE)
        return extra
    else: print("not enough coins")


def target_drink (selection, payment):
    if selection == "espresso":
        remainder = change(selection, payment)
        print(f"Here is you espresso with your change being ${remainder}")
    elif selection == "latte":
        remainder = change(selection, payment)
        print(f"Here is you latte with your change being ${remainder}")
    elif selection == "cappuccino":
        remainder = change(selection, payment)
        print(f"Here is you cappuccino with your change being ${remainder}")

another = 'yes'
while another == 'yes':
    selection = welcome_screen()
    payment = insert_coins()
    change(selection, payment)
    target_drink(selection, payment)
    another = input("Would you like another drink? (type 'yes' or 'no'): ")

print("Enjoy your coffee!")