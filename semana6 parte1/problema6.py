#Contador de Ocurrencias de una Subcadena: Diseña una función que tome una cadena y
# una subcadena, y cuente cuántas veces aparece la subcadena en la cadena principal. 
def cont(txt,tx):
    n=txt.count(tx)
    return n


txt=input("ingrese una texto: ").lower()
tx=input("ingrese lo que quiere buscar en el texto ").lower()
x=cont(txt,tx)
x=txt.count(tx)
print("lo que busca en el texto aparece: ",x)
