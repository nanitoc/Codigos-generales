# calculator
import os
from art import logo
print(logo)
# adding
def add(n1,n2):
    return n1+n2
# subtract
def sub(n1,n2):
    return n1-n2   
# dividing
def div(n1,n2):
    return n1/n2 
# multiply
def mult(n1,n2):
    return n1*n2

operations={                                    #Dictionary to call function
'+':add,
'-':sub,
'*':mult,
'/':div
}
next='n'
while True:
    if next=='n':   
        while True:                                         #loop para asegurar que entre un numero
            num1=input('\nwhat is the firts number?: ')
            try:
                num1=float(num1)
                break
            except:
                print('Valor invalido, introduzca un numero')

    for x in operations:                                       #for para printear las operaciones disponible
        print(x)
    while True:                                                    #loop para asegurar que seleccione un simbolo 
        symbol=input('Pick an operation: ')
        if symbol in operations:
            break
    
    while True:                                                 #loop para asegurar que entre un numero
            num2=input('\nwhat is the next number?: ')
            try:
                num2=float(num2)
                break
            except:
                print('Valor invalido, introduzca un numero')

    
    if next=='n':                                               #nueva operacion
        result=operations[symbol](num1,num2)                      #operacion para llamar la funcion seleccionada del diccionario
        print(f"{num1} {symbol} {num2} = {result}")                 #printeo el resultado con la nueva operacion
        
    else:                                                         #operacion con el resultado anterior
        print(f"{result} {symbol} {num2} = {operations[symbol](result,num2)}")                #printeo el resultado de la operacion con el result anterior
        result=operations[symbol](result,num2)

    while True:                                             #loop para asegurar que seleccione y or n
     next=input("\ntype 'y' if you want to use the result, type 'n' if you want to do a new operation: ").lower()
     if next=='y' or next=='n':
         break
    if next=='n':
        os.system('cls')
