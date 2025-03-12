#Cálculo de Distancias entre Puntos: Implementa una función que tome dos puntos en el
#  plano (tuplas (x1, y1) y (x2, y2)) y calcule la distancia euclidiana entre ellos. 
def distancia(c1,c2):
    x1, y1=c1
    x2, y2=c2
    dis=((x2-x1)**2+(y2-y1)**2)**(1/2)

    return dis


for i in range(2):
    x=int(input(f"ingrese el punto x{i+1} "))
    y=int(input(f"ingrese el punto y{i+1} "))
    if i == 0:
        coordenada1=(x,y)
    else:
        coordenada2=(x,y)

dis=distancia(coordenada1, coordenada2)
print(f"la distancia es de {dis}")
