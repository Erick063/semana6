#Implementa una función que captura el contenido de dos matrices (listas de listas) de 3 x 3 elementos.
#  Realiza la suma de ambas matrices e imprime su resultado. 

def sumat(matriz1,matriz2):
    matriz=[]
    for i in range (3):
        fila=[]
        for j in range (3):
            fila.append(matriz1[i][j]+matriz2[i][j])
        matriz.append(fila)
    for k in matriz:
        print(" ".join(map(str, k)))
    return matriz

matriz1 = [
    [4, 4, 4],
    [3, 3, 3],
    [2, 2, 2]
]

matriz2 = [
    [6, 6, 6],
    [7, 7, 7],
    [8, 8, 8]
]
matriz_suma=sumat(matriz1, matriz2)

