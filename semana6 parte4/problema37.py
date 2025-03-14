#Registro de Compras en una Tienda: Diseña un programa que permita al usuario ingresar
# información sobre las compras realizadas en una tienda. Cada compra se representa 
# como una tupla (producto, cantidad, precio_unitario). Calcula el total gastado por el cliente. 
suma=0
compra=[]
can=int(input("ingrese la cantidad de productos comprados "))
for i in range(can):
    prod=input("ingrese el nombre del producto ")
    cant=int(input("ingrese la cantidad comprada"))
    precio=int(input("ingrese el precio unitario del producto"))
    com=(prod, cant, precio)
    compra.append(com)
    suma+=precio*cant
print("el total gastado es de ", suma)
print(compra)