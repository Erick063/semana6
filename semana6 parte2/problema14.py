#Escribe una función que tome una matriz de 3 x 3 y devuelva su matriz transpuesta (intercambiando filas por columnas). 
def transpuesta(matriz):
    matriztra=[]
    lista1=[]
    lista2=[]
    lista3=[]
    for i in range(3):
        lista1.append(matriz[i][0])
        lista2.append(matriz[i][1])
        lista3.append(matriz[i][2])
    matriztra.append(lista1)
    matriztra.append(lista2)
    matriztra.append(lista3)
    for k in matriztra:
        print(" ".join(map(str, k)))
    return matriztra

matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]
x=transpuesta(matriz)
print(x)