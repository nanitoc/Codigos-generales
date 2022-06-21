# Dada una cadena de caracteres, imprime la cantidad de caracteres que se repiten en secuencia en la misma.
string="ssabsdddssssaab"
b="0"
i=1
#bucle para ir por cada caracter del string
for x in string:
    if x==b:                    # condicion para ver si el caracter es igual al anterior
        i+=1
    elif i!=1:                     # condicion para cuando termina la sucesion del caracter
        print(f"{b} : {i}")     # imprimo el caracter y las veces que se repitio
        i=1
    b=x                         # b sera igual al caracter anterior

