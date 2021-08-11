#Borron para practicas de OOP

# from turtle import Turtle, Screen, exitonclick, color


# timy = Turtle()
# timy.shape("turtle")

# my_screen = Screen()
# timy.color("#285078", "#a0c8f0")
# timy.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmender"])
table.add_column("TYPE",["Electric","Water","Fire"])
table.align='l'
print(table)