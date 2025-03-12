#Reversión de Palabras en una Frase: Escribe un programa que tome una frase 
# y devuelva una nueva frase con las palabras invertidas. Por ejemplo, 
# si la entrada es “Hola mundo”, la salida debería ser “aloh odnum”. 
txt=input("ingrese un texto " )
lista=list(txt.split())
lista.reverse()
tx=" ".join(lista)
revers=tx[::-1]
print("la el texto invertido es ", revers)