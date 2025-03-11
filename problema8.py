#Ordenamiento de Palabras por Longitud: Crea una función que tome una lista de palabras y
# las ordene de acuerdo con su longitud, de la más corta a la más larga. 
def lon(txt):
    lista=list(txt.split())
    lista.sort(key=len)
    return lista

txt=input("ingrese palabras separadas con espacio: ")
x=lon(txt)
print(x)

