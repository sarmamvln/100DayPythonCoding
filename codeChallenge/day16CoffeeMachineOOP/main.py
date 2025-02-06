from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import  PrettyTable
is_on=True

menu= Menu()
brewCoffe= CoffeeMaker()
ledger= MoneyMachine()

outlineTable= PrettyTable()

brewCoffe.report()

while is_on:
    options= menu.get_items()
    choice= input(f"What would you like? ({options}) : ")
    if(choice=="off"):
        is_on=False
    elif choice=="report":
        brewCoffe.report()
        ledger.report()
    else:
        drink= menu.find_drink(choice)
        if brewCoffe.is_resource_sufficient(drink) and ledger.make_payment(drink.cost):
            brewCoffe.make_coffee(drink)

