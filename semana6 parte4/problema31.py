#Diccionario de Precios de Productos: Implementa un programa que almacene los precios de diferentes
#  productos en un diccionario. El usuario debe poder buscar el precio de un producto dado su nombre. 
def agregar():
    nom=input("ingrese el nombre del producto ").capitalize()
    precio=int(input("ingrese el precio del producto "))
    if nom in diccionario:
        print(" el producto ya existe ")
    else:
        diccionario[nom] = precio
        print(" el producto ha sido agregado ")

def eliminar():
    nom = input("ingrese el nombre del producto a eliminar ").capitalize()
    if nom in diccionario:
        del diccionario[nom]
        print(" el producto ha sido eliminado")
    else:
        print(" el producto no existe") 

def buscar():
    nom = input("ingrese el producto a buscar ").capitalize()
    if nom in diccionario:
        print(f" {nom}: {diccionario[nom]}")
    else:
        print("el producto no se encontro")

diccionario={}

while True:
    print("1. agregar producto")
    print("2. eliminar producto")
    print("3. buscar producto")
    print("4. salir")
    opcion = int(input("ingrese una opcion "))
    if opcion == 1:
        agregar()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        buscar()
    elif opcion == 4:
        break
    else:
        print("error. ingrese una opcion valida")

