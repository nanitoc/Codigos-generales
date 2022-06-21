lista=[1, "numero", 100, "casa"] 

def sum_number(entrada):
    result=0
    for x in lista:                     # Bucle para navegar por cada caracter
        try:                            # intenta convertir el elemento si es posible es un numero
            int(x)
            condicion=True
        except:                         # si no fue posible no es un numero
            condicion=False
        if condicion:                   # evalulo la condicion
            result+=x                   # sumo los numeros
    print(result)                       # imprimo el resultado

sum_number(lista)                       # llamo la funcion