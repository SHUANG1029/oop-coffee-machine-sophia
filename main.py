from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

make_coffee = CoffeeMaker()
drink = Menu()
money = MoneyMachine()

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        make_coffee.report()
    else:
        MenuItem = drink.find_drink(choice)
        if MenuItem is not None:
            if make_coffee.is_resource_sufficient(MenuItem):
                if money.make_payment(MenuItem.cost):
                    money.report()
                    make_coffee.make_coffee(MenuItem)
                    print("pass here")
        else:
            is_on = False
