# 1. Crea una clase que haga una suma factorial de cualquier numero la clase se debe llamar factorial
# Ejecución. Factorial(3)
#  Resultado: 6

# creacion de la clase
class factorial: 

    # Funcion de la clase                       
    def Sum_Factorial(self,numero):             # Definicion de la funcion
        result=numero                           
        while numero > 1:                       # Bucle para calcular el factorial
            numero-=1                           
            result*=(numero)                    # operacion para calcular el factorial
        print(f"El resultado es: {result}")     # imprimo el resultado

while True:                                     # bucle principal
    cal_fact= factorial()                       
    cal_fact.Sum_Factorial(int(input("Type a number: ")))

