#Contador de Palabras en un Texto: Diseña un programa que tome un párrafo o un texto largo
# y cuente cuántas veces aparece cada palabra. Utiliza un diccionario para almacenar las 
# palabras y sus frecuencias. Al finalizar, recorre e imprime el contenido del diccionario con un ciclo.  

txt= input("ingrese un texto " )
lista=list(txt.split())
dicionario={}
for i in lista:
    suma=0
    for j in lista:
        if i == j:
            suma=suma+1
    dicionario[i]=suma
con=set(lista)
for i in con:
    print(f"la palabra {i} aparece un total de {dicionario[i]}")