import random
import os
from art import logo
os.system('cls')

#Lists
cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
User_score=[]
Pc_score=[] 
pc="Computer"
user="You"

#funcion para dar una carta a la lista en el argumento
def get_a_cart():
    list=random.choice(cards)
    
    return list
#Para printear scores
def show_scores():
    print(f"Your cards: {User_score}, current score: {sum(User_score)}")
    print(f"Computer's firts card:{Pc_score[0]}")

#para printear el ganador
def result(winner):
    os.system('cls')
    print(logo)
    print(f"\n\nYour final hand: {User_score}, final score: {sum(User_score)}")
    print(f"Computer's final hand: {Pc_score}, final score: {sum(Pc_score)}")
    if winner=="draw":
        print("there's a Draw ")
    else:
        print(f"{winner} WON")

#--------funcion  principal------
def play():
    os.system('cls')
    print(logo)
    User_score.clear()
    Pc_score.clear()
    draw_a_card="y"
    # 2 cartas inicialmente al user & dealer
    for x in range(1,3):
        x=get_a_cart()
        #si sale una A y la suma se pasa de 21, la A valdra 1
        if x==11 and (sum(User_score)+11)>21:
            User_score.append(1)   #se le agrega 1 en vez de 11
        #si la suma de 11 no pasa de 21 se le agrega 11
        else:
            User_score.append(x)
        x=get_a_cart()
        #si sale una A y la suma se pasa de 21, la A valdra 1
        if x==11 and (sum(Pc_score)+11)>21:
            Pc_score.append(1)   #se le agrega 1 en vez de 11
        #si la suma de 11 no pasa de 21 se le agrega 11
        else:
            Pc_score.append(x)


    show_scores()
    #pruebo si hay un ganador
    if sum(Pc_score)==21:
        result(pc)
    elif sum(User_score)==21:
        result(user)
    else:


        #loop para ver si quiere otra carta
        while draw_a_card=="y":
            
            #validacion de datos (solo acepta "y" or "n")
            while True:
                draw_a_card=input("Type 'y' to get another card, type 'n' to pass:")
                if draw_a_card=="y" or draw_a_card=="n":
                    break
            #si el usario toma otra carta
            if draw_a_card=="y":
                x=get_a_cart()
                #si sale una A y la suma se pasa de 21, la A valdra 1
                if x==11 and (sum(User_score)+11)>21:
                    User_score.append(1)   #se le agrega 1 en vez de 11
                #si la suma de 11 no pasa de 21 se le agrega 11
                else:
                    User_score.append(x)
                show_scores()     #printeo el score presente
                if sum(User_score)>21:
                    result(pc)          #gana la pc
                    draw_a_card="n"     #el usuario ha perdido y rompe el bucle de preguntar si quiere otra carta          
            #si el usario pasa de cartas
            else:
                draw_a_card="n"     #el usuario pasa de cartas entonces se rompe el while loop 
                while sum(Pc_score)<17: #mientras el score de la pc sea menor a 17 dale una carta
                    x=get_a_cart()
                    #si sale una A y la suma se pasa de 21, la A valdra 1
                    if x==11 and (sum(Pc_score)+11)>21:
                        Pc_score.append(1)   #se le agrega 1 en vez de 11
                    #si la suma de 11 no pasa de 21 se le agrega 11
                    else:
                        Pc_score.append(x)

                if sum(User_score)==sum(Pc_score):  #hay un empate
                    result("draw")          #printeo un empate
                elif sum(User_score)>sum(Pc_score):   #gana el usuario
                    result(user)
                elif sum(Pc_score)<=21:             #gana la pc
                    result(pc)
                else:
                    result(user)
            


    #validacion de datos (solo acepta "y" or "n")
    while True:
        play_again=input("type 'y' if you want to play again, type 'no' if not:").lower()
        if play_again=="y" or play_again=="n":
            break
    #si el usurio quiere jugar hay una recursion de la funcion play
    if play_again=="y":
        os.system('cls')
        play()
    #si no, se termina la funcion
    else:
        return

#validacion de datos
while True:
    start=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start=="y" or start=="n":
            break
if start=='y':
    play()
    print("thank you for play")
else:
    print("See You soon")



    


