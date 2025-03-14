#Ordenamiento de Puntos en el Plano: Implementa una función que tome una lista de puntos en el
#  plano (representados como tuplas (x, y)) y los ordene según su distancia al origen (punto (0, 0)). 
def distancia(c):
    x, y=c
    dis=((x)**2+(y)**2)**(1/2)

    return dis

def ordenar(lista):
    return sorted(lista, key = distancia)


puntos = [(3, 4), (1, 1), (-2, -2), (0, 5), (7, 8)]
ordenados = ordenar(puntos)
print("los puntos ordenados por su distancia al origen es ", ordenados)
