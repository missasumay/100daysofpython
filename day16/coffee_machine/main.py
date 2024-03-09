from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
bank = MoneyMachine()
available_drinks = Menu()
coffee = True

while coffee:
  print(available_drinks.get_items())
  order_name = input("What drink would you like? ")

  if order_name == "off":
     coffee = False # turns off
  elif order_name == "report": #prints report
     coffee_machine.report()
     bank.report()
  else:
    chosen_drink = available_drinks.find_drink(order_name) # assign name of the drink to the variable

    if coffee_machine.is_resource_sufficient(chosen_drink):
        if bank.make_payment(chosen_drink.cost):
            coffee_machine.make_coffee(chosen_drink)