from art import Logo,MENU,resources

# Global variables
options=["espresso","latte","cappuccino"]
money=0


#funcion para ver si hay con que preparar el cafe
def check_resources(sel):
    result=0
    condicion=True
    for x in MENU[sel]["ingredients"]:
        result=resources[x]-MENU[sel]["ingredients"][x]
        if result<0:  condicion=False
    return condicion

#funcion para actualizar resources
def updateresouces(sel2): 
    for x in MENU[sel2]["ingredients"]:
        resources[x]=resources[x]-MENU[sel2]["ingredients"][x]     
    return

#funcion para que solo se entren numeros
def check_number(coin):
    while True:                                                 #loop para asegurar que entre un numero
        num=input(f'\nhow many {coin}?: ')
        try:
            num=float(num)
            break
        except:
            print('Valor invalido, introduzca un numero')
    return num

def making(sel):   #TODO: desarrollar funcion para hacer el cafe
    #proceso para introducir monedas
    global money
    print("\nPlease insert coins.")
    q=check_number("quaters")   #quaters
    d=check_number("dimes")     #dimes
    n=check_number("nickles")   #nickles
    p=check_number("pennies")   #pennies
    total=q*0.25+d*0.10+n*0.05+p*0.01

    
    if total>=MENU[sel]["cost"]:        #si el dinero es suficiente ofrece el servicio
        change=round(total-MENU[sel]["cost"],2)
        print(f"Here is {change} in change.")
        print(f"Here is your {sel} ☕️. Enjoy!")
        money+=money+MENU[sel]["cost"]
        #update resources
        updateresouces(sel)

    else:                                #si el dinero no es suficiente 
        print("Sorry that's not enough money. Money refunded.")
    
    return
#funcion principal
def main():

    while True:                                             #loop para asegurar que seleccione y or n
        selection=input('\n\nWhat would you like? (espresso/latte/cappuccino): ').lower()
        if selection in options or selection=="report" or selection=="off": break
        else: print("Option invalida")

    if selection in options:       #se procesa el cafe seleccionado
        if check_resources(selection):
            making(selection)
        else: print("Sorry there is not enough water.")
       
    elif selection=="report":   #se imprime el reporte
        print(f"""
    water     : {resources["water"]} ml
    milk      : {resources["milk"]} ml
    coffee    : {resources["coffee"]} mg 
    Money     : {money} $                      """)
    else:                       #se selecciono off
        return "off"

while True:
 if main()=="off":
     break

print("Thank you")