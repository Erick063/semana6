#Fusión de Listas Ordenadas: Implementa una función que tome dos listas ordenadas 
# y las fusione en una nueva lista ordenada. Utiliza sort o sorted. 
def lis(lista1, lista2):
    lista=lista1+lista2
    return sorted(lista)
lista1=[1,2,3,6,8,9]
lista2=[4,7,11,12,15]
res=lis(lista1,lista2)
print("la nueva lista es ", res)
    