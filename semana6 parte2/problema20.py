#Intersección de Conjuntos: Implementa una función que tome dos conjuntos y devuelva su intersección. 
def interseccion(c1, c2):
    c3=c1&c2
    return c3

conjunto1={1,2,3,4,5,6,7,8,9}
conjunto2={6,7,8,9,10,11,12,13,14}
conjunto3=interseccion(conjunto1, conjunto2)
print(conjunto3)