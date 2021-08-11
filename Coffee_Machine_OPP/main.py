from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
options=["espresso","latte","cappuccino","report","off"]


def main():
    while True:                                             #loop para asegurar que seleccione y or n
        selection=input('\nWhat would you like? (espresso/latte/cappuccino): ').lower()
        if selection in options : break
        else: print("invalid Option")
    if 

    

os.system('cls')
print(Logo)
while True:
    if main()=="off":
        break
print("Thank you")