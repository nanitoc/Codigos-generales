#Step 1 

import random
from Hangman_words import word_list
from Hangmang_art import stages,logo
lives=6
print(logo)
Display=[]
chosen_word=random.choice(word_list)
for x in range(0,len(chosen_word)):
  Display.append("_")
print(" ".join(Display))
print(stages[lives])
guess='1'
while not "".join(Display)==chosen_word and lives>0:
    result=False
    guess=input('\nguess a letter: ').lower()

    while guess in Display:
        print(f'Your last chance was {guess}, select another letter')
        guess=input('\nguess a letter: ').lower()
        # if guess in Display:
        
    i=0
    for x in chosen_word:
        if x==guess:
            Display[i]=guess
            i+=1
            result=True

        else:
            i+=1

    print(" ".join(Display))

    if result==False:
        print(f'You have chosen {guess} and it is not on the word')
        lives-=1
        print(stages[lives])
    else:
        print(stages[lives])

      
if lives>0:
    print("You've WON")
else:
    print("You've Lost")