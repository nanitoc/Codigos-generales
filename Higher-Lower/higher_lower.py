import os
from data import data
from art import logo,vs
import random
A={}
B={}
score=0
#para seleccionar el numero ramdom
def select_random():
    while True:                   #bloqueo para que A y B no sean iguales
        x=random.randint(0,len(data))    #selecciono un numero random
        if data.index(A)!=x:    break      #si a y x son diferentes salgo del bucle
    return x

#para checkear si la respuesta es correcta
def check(selection):
    if A['follower_count'] > B ['follower_count']: greater='a'  # a es mayor
    else:   greater='b' # b es mayor
    if selection == greater : return True       #devuelvo verdadero si selecciono el correcto
    else: return False                          #falso si selecciono mal

#bucle principal
def main():
    global A,B,score
    B=data[select_random()]         #Selecciono un valor para B
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")    #printeo la opcion A a comparar
    print(vs)
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")    #printeo la opcion B a comparar

    while True:                                #bloqueo para que solo pueda entrar a o b
        sel=input("Who has more followers? Type 'A' or 'B': ").lower()
        if sel=='a' or sel=='b': break
    
    if check(sel):          #si selecciono bien
        os.system('cls')       #borro la pantalla
        print(logo)
        score+=1                #sumo uno al score
        print(f"You're right! Current score: {score}")  #printeo el score
        A=B                          #B pasara a ser A
        main()              #hago una recursion
    else:
        print(f"Sorry, that's wrong. Final score: {score}")     #printeo que perdio
        return



while True:
    os.system('cls')
    print(logo)
    A=data[random.randint(0,len(data))]         #selecciono un valor para A
    main()
    while True:                                             #loop para asegurar que seleccione y or n
        next=input("\ntype 'y' if you want to use the result, type 'n' if you want to do a new operation: ").lower()
        if next=='y' or next=='n':break
    if next=='n':break
print('Thank you for playing our Game')



