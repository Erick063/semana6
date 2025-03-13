#Registro de Puntajes de Jugadores: Implementa un programa que permita registrar los puntajes de 
# varios jugadores en un juego. Cada jugador tiene un nombre y un puntaje asociado.
# Utiliza un diccionario para almacenar e imprimir esta información. 
dict={}
x=input("ingrese la cantidad de jugadores ")
for i in range(int(x)):
    nom=input("ingrese el nombre del jugador ")
    p=int(input("ingrese el puntaje del jugador "))
    dict[nom]=p
print(dict)