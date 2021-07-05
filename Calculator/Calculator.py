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
# next='n'
def calculator():

    while True:                                         #loop para asegurar que entre un numero
        num1=input('\nwhat is the firts number?: ')
        try:
            num1=float(num1)
            break
        except:
            print('Valor invalido, introduzca un numero')

    for x in operations:                                       #for para printear las operaciones disponible
        print(x)
    
    should_continue=True
    while should_continue:                                              #Loop para operar con el resultado anterior
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

        
                                                      #nueva operacion
        result=operations[symbol](num1,num2)                      #operacion para llamar la funcion seleccionada del diccionario
        print(f"{num1} {symbol} {num2} = {result}")                 #printeo el resultado de la operacion

        while True:                                             #loop para asegurar que seleccione y or n
            next=input("\ntype 'y' if you want to use the result, type 'n' if you want to do a new operation: ").lower()
            if next=='y' or next=='n':
                break
        if next=='y':                                      #igualo el resultado a el num 1
            num1=result
        else:
            should_continue=False
            calculator()                                #recurcion

calculator()
