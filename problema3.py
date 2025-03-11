#Contador de Vocales y Consonantes: Diseña una función que tome una palabra y cuente 
#cuántas vocales y cuántas consonantes contiene. Considera tanto mayúsculas como minúsculas
def cont(palabra):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    cont1 = 0
    cont2 = 0
    for i in palabra:
        if i in vocales:
            cont1 += 1
        elif i in consonantes:
            cont2 += 1
    
    return cont1, cont2

palabra = input("Ingresa una palabra: ")
v, c = cont(palabra)
print(f"vocales: {v}, consonantes: {c}")
