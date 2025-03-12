#Producto Escalar de Vectores: Diseña un programa que tome dos vectores (listas de números del tipo i_x, i_y, i_z) 
# y calcule su producto escalar. Los vectores deben tener la misma longitud. 
lista=[]
for i in range(2):
    lista1=[]
    x=int(input(f"ingrese el valor de x del vector {i+1} "))
    y=int(input(f"ingrese el valor de y del vector {i+1} "))
    z=int(input(f"ingrese el valor de z del vector {i+1} "))
    lista1.append(x)
    lista1.append(y)
    lista1.append(z)
    lista.append(lista1)
sum=0
for j in range(3):
    sum=sum+(lista[0][j]*lista[1][j])
print(sum)