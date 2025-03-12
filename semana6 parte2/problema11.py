#Matriz de Ceros y Unos: Diseña un programa que cree una matriz de tamaño n x m (donde n y m son números enteros dados)
#  y la inicialice con ceros y unos alternados (como un tablero de ajedrez). 

def matriz(n, m):
    matriz=[]
    for i in range(n):
        fila=[]
        for j in range(m):
            fila.append((i+j)%2)
        matriz.append(fila)    
    for k in matriz:
        print(" ".join(map(str, k)))
    
    return matriz

n = int(input("Ingrese el número de filas: "))
m = int(input("Ingrese el número de columnas: "))

matriz = matriz(n, m)
