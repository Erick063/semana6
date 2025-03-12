#Búsqueda de Elemento en Matriz: Crea una función que tome una matriz y un elemento.
# Verifica si el elemento está presente en la matriz y devuelve su posición (fila y columna). 
def busqueda(matriz, elemento):
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            lista1=[]
            if matriz[i][j] == elemento:
                x=str(f"{i+1}:{j+1}")
                lista1.append(x)
                lista.append(lista1)
    return lista

matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]
elemento=int(input("ingrese el elemento que quiere buscar "))

pos=busqueda(matriz, elemento)
if pos:
    print("el elemento si y su posicion(es) es ", pos)
else:
    print("la lista no tiene ese elemento")