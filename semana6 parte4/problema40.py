#Registro de Ventas por Producto y Mes: Escribe un programa que almacene información 
# sobre las ventas de una tienda. Cada venta se representa como un diccionario con las
#  claves “producto”, “mes” y “cantidad_vendida”. 
# Lista para almacenar los registros de ventas
def venta(producto, mes, cantidad_vendida):
    ven = {
        "producto": producto,
        "mes": mes,
        "cantidad_vendida": cantidad_vendida
    }
    ventas.append(ven)

ventas = []
num=int(input("ingrese el numero de ventas "))
for i in range (num):
    producto=input("ingrese el producto ")
    mes=int(input("ingrese el mes "))
    cantidad_vendida=int(input("ingrese la cantidad vendida "))
    venta(producto, mes, cantidad_vendida)

for venta in ventas:
    print(f"Producto: {venta['producto']}, Mes: {venta['mes']}, Cantidad Vendida: {venta['cantidad_vendida']}")
