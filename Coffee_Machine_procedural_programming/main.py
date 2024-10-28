from resources import MENU
from resources import COINS
from resources import resources

money = 0

def check_resources(coffee):
    """Checks if there are enough resources. If not, print related error and return 1. Else 0."""
    for item in MENU[coffee]["ingredients"]:
        if resources[item] < MENU[coffee]["ingredients"][item]:
            print(F"Sorry, there is not enough {item}.")
            return False
    else:
        return True

def print_report():
    """Print resources and income"""
    global money
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print("Money: $ %.2f" % money)

def print_prices():
    """Print prices"""
    print("Espresso: $%.2f" % MENU["espresso"]["cost"])
    print("Latte: $%.2f" % MENU["latte"]["cost"])
    print("Cappuccino: $%.2f" % MENU["cappuccino"]["cost"])

def take_money(selected_drink):
    """Take coins and calculate if enough for ordered drink.
    if not: print error and return 1.
    if yes: save money, print change, return 0"""
    global money
    coins = ["quarters", "dimes", "nickles", "pennies"]
    inserted_amount = 0
    print("Please insert coins.")
    for coin in coins:
        while True:
            try:
                given_coins = int(input(f"How many {coin}?: "))
                break
            except ValueError:
                print("Invalid value. Please insert a total number such as 1.")
        inserted_amount += given_coins * COINS[coin]
    if inserted_amount < MENU[selected_drink]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    change = inserted_amount - MENU[selected_drink]["cost"]
    if change > 0:
        print(f"Here is {round(change, 2)} in change.")
    money += MENU[selected_drink]["cost"]
    return True

def make_coffee(coffee):
    """Reduces resources accordingly. Print coffee message."""
    for item in MENU[coffee]["ingredients"]:
        resources[item] -= MENU[coffee]["ingredients"][item]
    print(f"Here is your {coffee}. Enjoy! <3")

while True:
    extra_functions = ["report", "prices", "off"]
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    while choice not in MENU and choice not in extra_functions:
        choice = input(f"Invalid choice.Please select from: (espresso/latte/cappuccino): ")
    if choice == "off":
        exit()
    if choice == "report":
        print_report()
        continue
    if choice == "prices":
        print_prices()
        continue
    if not (
            check_resources(choice)):
        continue
    if not take_money(choice):
        continue
    make_coffee(choice)


