#Step 1 
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6

word_list = ["aardvark", "baboon", "camel"]
Display=[]
chosen_word=random.choice(word_list)
print(chosen_word)
for x in range(0,len(chosen_word)):
  Display.append("_")
print(" ".join(Display))
print(stages[lives])

while not "".join(Display)==chosen_word:
    result=False
    guess=input('\nguess a letter: ').lower()
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
        lives-=1
        print(stages[lives])
    else:
        print(stages[lives])
    if lives==0:
        break
if lives>0:
    print("You've WON")
else:
    print("You've Lost")