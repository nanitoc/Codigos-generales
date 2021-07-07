#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
options=[letters,symbols,numbers]
Passwordlen=nr_letters+nr_numbers+nr_symbols
print(f'your password will have {Passwordlen} characters')
password=[]
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
n=0
cl=0
cs=0
cn=0
while len(password)<Passwordlen:
  r1=random.randint(0,2)
  if cl!=nr_letters and r1==0 or cs!=nr_symbols and r1==1 or cn!=nr_numbers and r1==2:
    r2=random.randint(0,len(options[r1]))-1
    password.append(options[r1][r2])
    if r1==0:
      cl+=1
    elif r1==1:
      cs+=1
    elif r1==2:
      cn+=1
n="".join(password)
print(f'\nYour Password is:\n\n{n}')

