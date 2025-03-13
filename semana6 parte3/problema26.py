#Eliminación de Elementos en Conjunto: Implementa un programa que tome un conjunto 
#y elimine un elemento específico si está presente. 


con={1,2,2,3,4,4,5,6,7,8,9,0}
el=input("ingrese el elemento que quiere eliminar  ")
con.discard(el)
print(con)