from typing import Tuple
from art import logo, alphabet
again=True
print(logo)

import os
os.system('cls')

# Funcion que desplaza las letras de la palabra
def caesar(word,shift):
    New_word=''

    for x in word:                                              #accedo a cada caracter de la palabra
        if x in alphabet:                                         #pregunto si el caracter esta en el abecedario
            new_index=alphabet.index(x)
            if direction=='encode':                              #si quiero codificar
                New_word+=alphabet[new_index+shift]
            else:
                New_word+=alphabet[new_index-shift]             #si quiero descodificar
        else:
            New_word+=x                                         #si el caracter no pertenece al abcedario se agrega directamente
    if direction=='encode':
        print(f'here is the encode result: {New_word}\n')
    else:
        print(f'here is the decode result: {New_word}\n') 
    

#Bucle principal
while again==True:
    r=True
    #bloqueo de entrada de direction
    while r:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction=='encode' or direction=='decode':
            r=False
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26                                                       #operacion realizada por si entran un shift mayor a 26, el shift sera igual a el resto
    caesar(text,shift)
    r=True

    #bloque de entrada de yes or no
    while r:
        block=input("Type 'yes' if want to go again, Otherwise type'no': \n").lower()
        if block=='no' or block=='yes':
            r=False
    if block=='no':
            again=False                                                    #Si el usuario selecciona no, se rompe el bucle principal
            print('\nThank you so much')



