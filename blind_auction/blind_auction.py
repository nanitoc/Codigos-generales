
from art import logo
import os
os.system('cls')
print(logo)
print('Welcome to the Secret Auction Program\n\n')
people={}       #dictionary que registrara los bidders

#funcion para agregar bidders al dict
def add_new_bidder(key,value):
  people.update({key : value})

#funcion para calcular el ganador
def cal_winner(dict):
    winner=max(dict,key=people.get)
    return winner
# bucle principal
while 1:
    name=input('\nwhat is yout name?  \n').lower()
    price=int(input("\nwhat's your price?  $\n").lower())
    add_new_bidder(name,price)
    
    r=True
    while r:                                                                        #limito a entrada yes o no
        stop=input("\nare there any other bidder? Type 'yes' or 'no'\n").lower()                        
        if stop=='no'or stop=='yes':
            r=False
    if stop=='no':
        winner=cal_winner(people)
        break
    os.system('cls')

#printeo al ganado
print(f"\n\n---->The winner is {winner.capitalize()} with a bid of ${people[winner]}<----\n\n")