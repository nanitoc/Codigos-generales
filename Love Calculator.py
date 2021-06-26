while 1:
  print('Welcome to the love calculator!\n')
  name1=input('what is your name? \n')
  name2=input('what is their name? \n')
  name=name1+name2
  cuenta=[]
  cuenta1=[]
  decena=0
  unidad=0
  #true
  for x in name.upper():
    cuenta.append('TRUE'.count(x))
  decena=sum(cuenta)

  #love
  for x in name.upper():
    cuenta1.append('LOVE'.count(x))

  unidad=sum(cuenta1)

  probabilidad=str(decena)+str(unidad)
  pro=int(probabilidad)

  if pro <10 or pro>90:
    print(f'Your score is {pro}%, you go together like coke and mentos\n\n')

  elif pro>=40 and pro<=50:
    print(f'Your score is {pro}%, you are alright together\n\n')
  else:
    print(f'your score is {pro}%\n\n')