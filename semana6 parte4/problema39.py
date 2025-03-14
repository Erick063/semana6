#Agenda de Contactos Mejorada: Implementa un programa que permita agregar, buscar y eliminar contactos en una agenda.
#  Cada contacto tiene un nombre, un número de teléfono y una lista de correos electrónicos. Usa una lista de diccionatos. 
def agregar():
    dicc = {}
    correos = []
    nom=input("ingrese el nombre del contacto ").capitalize()
    tel = input("ingrese el número de teléfono ")
    c=int(input("ingrese la cantidad de correos"))
    for i in range(c):
        correo=input("ingrese el correo electronico ")
        correos.append(correo)

    dicc["telefono"] = tel
    dicc["correos"] = correos
    if nom in agenda:
        print(" el contacto ya existe ")
    else:
        agenda[nom] = dicc

def buscar():
    nom = input("ingrese el nombre a buscar ").capitalize()
    if nom in agenda:
        contacto=agenda[nom]
        print(f"nombre: {nom}")
        print(f"telefono: {contacto['telefono']}")
        print("correos electronico:")
        for correo in contacto["correos"]:
            print(f"{correo}")
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


