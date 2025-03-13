#Palabras sin Vocales: Crea una función que tome una cadena y devuelva un 
# conjunto con las consonantes presentes en ella. 
def consonantes(txt):
    con=set(txt)
    lista = ['a','e','i','o','u'," "]
    for i in lista:
        con.discard(i)
    return con
txt=input("ingrese un texto  ")
con=consonantes(txt)
print(con)