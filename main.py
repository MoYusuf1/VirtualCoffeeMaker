import data

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

ESPRESSO_PRICE = 1.50
LATTE_PRICE = 2.50
CAPPUCCINO_PRICE = 3.0

machine_resources = [data.resources['water'], data.resources['milk'],
                         data.resources['coffee']]

print(machine_resources)


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
    else:
        print("not enough coins")


def target_drink(selection, payment, machine_resources):
    if selection == "espresso":
        if machine_resources[0] < 50 or machine_resources[2] < 18:
            print("Machine doesn't have enough resources to make an espresso")
            print(f"*Gives {payment} back to you*")
            return
        else:
            machine_resources[0] -= 50
            machine_resources[1] -= 18
        remainder = change(selection, payment)
        print(f"Here is you espresso with your change being ${remainder}")
    elif selection == "latte":
        if machine_resources[0] < 200 or machine_resources[1] < 150 or \
                machine_resources[2] < 24:
            print("Machine doesn't have enough resources to make a latte")
            print(f"*Gives {payment} back to you*")
            return
        else:
            machine_resources[0] -= 200
            machine_resources[1] -= 150
            machine_resources[2] -= 24
        remainder = change(selection, payment)
        print(f"Here is you latte with your change being ${remainder}")
    elif selection == "cappuccino":
        if machine_resources[0] < 250 or machine_resources[1] < 100 or \
                machine_resources[2] < 24:
            print("Machine doesn't have enough resources to make a cappuccino")
            print(f"*Gives {payment} back to you*")
            return
        else:
            machine_resources[0] -= 250
            machine_resources[1] -= 100
            machine_resources[2] -= 24
        remainder = change(selection, payment)
        print(f"Here is you cappuccino with your change being ${remainder}")


another = 'yes'
while another == 'yes':
    print(f"Current machine resources are {machine_resources}")
    selection = welcome_screen()
    payment = insert_coins()
    change(selection, payment)
    target_drink(selection, payment, machine_resources)
    another = input("Would you like another drink? (type 'yes' or 'no'): ")

print("Enjoy your coffee!")
