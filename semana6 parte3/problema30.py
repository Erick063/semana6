#Agenda de Contactos: Diseña un programa que permita al usuario agregar, buscar y eliminar 
# contactos en una agenda. Cada contacto tiene un nombre y un número de teléfono. 
# Diccionario para almacenar los contactos
def agregar():
    nom=input("ingrese el nombre del contacto ").capitalize()
    tel = input("ingrese el número de teléfono ")
    if nom in agenda:
        print(" el contacto ya existe ")
    else:
        agenda[nom] = tel
        print(" contacto ha sido agregado ")

def buscar():
    nom = input("ingrese el nombre a buscar ").capitalize()
    if nom in agenda:
        print(f" {nom}: {agenda[nom]}")
    else:
        print("el contacto no se encontro")

def eliminar():
    nom = input("ingrese el nombre del contacto a eliminar ").capitalize()
    if nom in agenda:
        del agenda[nom]
        print(" contacto ha sido eliminado")
    else:
        print(" el contacto no existe")

agenda={}
while True:
    print(" AGENDA DE CONTACTOS")
    print("1. agregar contacto")
    print("2. buscar contacto")
    print("3. eliminar contacto")
    print("4. salir")
    opcion = int(input("ingrese una opcion "))
    if opcion == 1:
        agregar()
    elif opcion == 2:
        buscar()
    elif opcion == 3:
        eliminar()
    elif opcion == 4:
        break
    else:
        print("error. ingrese una opcion valida")


