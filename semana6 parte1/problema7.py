#Formateo de Nombres Completos: Escribe un programa que tome un nombre completo 
#(por ejemplo, “Juan Pérez Gómez”) y devuelva las iniciales en mayúsculas (por ejemplo, “JPG”). 
txt=input("ingrese el nombre: ")
lista=list(txt.split())
nom=""
for i in range (len(lista)):
    x=lista[i][0]
    nom+=x
print(nom.upper())