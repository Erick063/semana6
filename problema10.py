#Eliminación de Elementos según Condición: Diseña una función que tome 
# una lista y elimine todos los elementos que no sean pares. 
def np(lista):
    newlista=[]
    for i in range(len(lista)):
        if lista[i]%2==0:
            newlista.append(lista[i])
    return newlista

lista=[1,2,3,4,5,6,7,8,9,0,12,14,42,554,323,233,235,653]
lista1=np(lista)
print("la lista sin elementos que no son pares", lista1)