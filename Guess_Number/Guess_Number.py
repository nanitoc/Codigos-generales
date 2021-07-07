import random
import os
os.system('cls')

def check(guess,number):
    if guess<number: 
        print("too Low \nGuess again.")
        return False
    elif guess>number:
        print("too High \nGuess again.")
        return False
    else:
        print(f"You got it! The answer is {number}")
        return True

def play():
    number=random.randint(1,101)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    print(f"shhh, the secret number is {number}")
    while True:
        level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level=='easy' or level=='hard': break
    if level=='easy': lives=10
    elif level=='hard': lives=5
    while True:
        print(f"You have {lives} attempts remaining to guess the number.")
        while True:                                                 #loop para asegurar que entre un numero
            guess=input('\nMake a guess: ')           
            try:
                guess=float(guess)
                break
            except:print('Valor invalido, introduzca un numero')
        lives-=1
        if check(guess,number) or lives==0: break
    if lives==0:
        print("You've run out of guesses, you lose.")
        return

while True:
    os.system('cls')
    play()
    while True:                                             #loop para asegurar que seleccione y or n
        next=input("\ntype 'y' if you want to use the result, type 'n' if you want to do a new operation: ").lower()
        if next=='y' or next=='n':break
    if next=='n':break
print('Thank you for playing our Game')



    

