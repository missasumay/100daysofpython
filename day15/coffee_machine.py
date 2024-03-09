import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
}

coffee_price = 0
payment = 0
change = 0
earned = 0
enough_resources = True
can_be_completed = True
enough_money = False

pennies = 0 # $0.01
nickles = 0 # $0.05
dimes = 0 # $0.10
quarters = 0 # $0.25

def set_coffee_price(coffee_type):
    global coffee_price
    global MENU

    coffee_price = MENU[coffee_type]['cost']

def count_payment(one_cent_amount, five_cents_amount, ten_cents_amount, twenty_five_cents_amount):
    global payment

    payment = round((0.01 * one_cent_amount) + (0.05 * five_cents_amount) + (0.1 * ten_cents_amount) + (0.25 * twenty_five_cents_amount), 2)

    print(f"You paid ${payment}.")

    return payment

def calc_change():
    global change
    global payment
    global coffee_price

    change = round((payment - coffee_price), 2)

    return

def pay(coffee_type):
    global pennies
    global nickles
    global dimes
    global quarters
    global coffee_price
    global enough_money
    global can_be_completed

    set_coffee_price(coffee_type)

    print(f"The price of your coffee will be ${coffee_price}.")
    print("Please insert coins.")

    quarters = int(input("How many quarters? ($0.25): "))
    dimes = int(input("How many dimes? ($0.10): "))
    nickles = int(input("How many nickles? ($0.05): "))
    pennies = int(input("How many pennies? ($0.01): "))

    count_payment(pennies, nickles, dimes, quarters)

    if payment > coffee_price:
        calc_change()
        print(f"Here is ${change} in change.")
        enough_money = True
        return enough_money
    elif payment < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
        enough_money = False
        return enough_money
    
    enough_money = True
    return enough_money

def reduce (coffee_type):
    global MENU
    global resources

def prep(coffee_type):
    global MENU
    global resources
    global can_be_completed
    global enough_money

    order_ingredients = MENU[coffee_type]['ingredients']

    if order_ingredients['water'] > resources['water']:
        print("Sorry, there is not enough water.")
        can_be_completed = False
    elif order_ingredients['coffee'] > resources['coffee']:
        print("Sorry, there is not enough coffee.")
        can_be_completed = False
    elif 'milk' in order_ingredients:
        if order_ingredients['milk'] > resources['milk']:
            print("Sorry, there is not enough milk.")
            can_be_completed = False
        else:
            pay(coffee_type)

        if enough_money:
            resources['water'] -= order_ingredients['water']
            resources['coffee'] -= order_ingredients['coffee']
            
            if 'milk' in coffee_type:
                resources['milk'] -= order_ingredients['milk']
            
            can_be_completed = True
        else:
            can_be_completed = False

    else:
        pay(coffee_type)

        if enough_money:
            resources['water'] -= order_ingredients['water']
            resources['coffee'] -= order_ingredients['coffee']
            
            if 'milk' in coffee_type:
                resources['milk'] -= order_ingredients['milk']
            
            can_be_completed = True
        else:
            can_be_completed = False

    return can_be_completed

def report():
    global resources
    global earned

    print(f"Water: {resources['water']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Milk: {resources['milk']}")
    print(f"Money: ${earned}")

def resupply():
    global resources
    global enough_resources

    resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
    }
    enough_resources = True


def coffee_machine():
    global can_be_completed
    global change
    global coffee_price
    global enough_resources
    global earned
    global enough_money

    while enough_resources:
        action = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if action == "report":
            report()
        elif action == "off":
            sys.exit()
        elif action == "resupply":
            resupply()
        elif action != "espresso" and action != "latte" and action != "cappuccino":
            print("Incorrect order. Please check your speling.")
            coffee_machine()
        else:
            prep(action)

            if enough_money and can_be_completed:
                earned += coffee_price
                print(f"Here is your {action} ☕. Enjoy!")
                enough_money = False
                can_be_completed = False

    while not enough_resources:
        action = input("Machine needs to be resupplied: ").lower()
        if action == "report":
            report()
        elif action == "off":
            sys.exit()
        elif action == "resupply":
            resupply()
            coffee_machine()
        elif action != "espresso" and action != "latte" and action != "cappuccino":
            print("Incorrect order. Please check your speling.")
            coffee_machine()


coffee_machine()