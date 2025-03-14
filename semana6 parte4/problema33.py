#Diccionario de Traducción de Palabras: Diseña un programa que permita al usuario ingresar palabras 
#en un idioma y sus traducciones en otro idioma. Utiliza un diccionario para almacenar esta información. 
diccionario={}
while True:
    print("1. agregar palabra y su traduccion")
    print("2. salir")
    opcion = int( input("ingrese una opcion " ) )
    if opcion == 1:
        palabra=input("ingrese la palabra ")
        traduccion=input("ingrese la traduccion ")
        diccionario[palabra] = traduccion
    else:
        break

