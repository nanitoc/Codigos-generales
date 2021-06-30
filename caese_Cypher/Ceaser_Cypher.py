from typing import Tuple
from art import logo, alphabet
again=True
print(logo)

def caesar(word,shift):
    New_word=''

    for x in word:
        if x in alphabet:
            new_index=alphabet.index(x)
            if direction=='encode':
                New_word+=alphabet[new_index+shift]
            else:
                New_word+=alphabet[new_index-shift]
        else:
            New_word+=x
    if direction=='encode':
        print(f'here is the encode result: {New_word}\n')
    else:
        print(f'here is the decode result: {New_word}\n') 
    

while again==True:
    r=True
    while r:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction=='encode' or direction=='decode':
            r=False
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    caesar(text,shift)
    r=True
    while r:
        again=input("Type 'yes' if want to go again, Otherwise type'no': \n").lower()
        if again=='no':
            r=False
            print('\nThank you so much')
        if again=='no' or again=='yes':
            r=False




