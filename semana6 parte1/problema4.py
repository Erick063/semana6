#Eliminación de Espacios Extra: Escribe un programa que tome una cadena con espacios adicionales y elimine 
# los espacios redundantes. Por ejemplo, si la entrada es “Hola        mundo”, la salida debería ser “Hola mundo”. 
txt=input("ingrese un texto " )
lista=list(txt.split())
tx=" ".join(lista)
print("el texto sin espacios extra es: ", tx)