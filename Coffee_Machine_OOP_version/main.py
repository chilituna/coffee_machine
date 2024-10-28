from string import printable

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
profit = MoneyMachine()
machine_is_on = True
while machine_is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "report":
        machine.report()
        profit.report()
    elif choice == "off":
        machine_is_on = False
    else:
        while menu.find_drink(choice) is None:
            choice = input(f"Please select from: ({menu.get_items()}): ")
        choice = menu.find_drink(choice)
        if machine.is_resource_sufficient(choice) and profit.make_payment(choice.cost):
                machine.make_coffee(choice)




