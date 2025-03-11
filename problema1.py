#Contador de Palabras en un Texto: Diseña un programa que tome 
#un párrafo o un texto largo y cuente cuántas palabras contiene.
#Considera que las palabras están separadas por espacios.
txt= input("ingrese un texto " )
lista=list(txt.split())
num=len(lista)
print("el numero de palabras es de ",num )