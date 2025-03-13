#Comprobación de Subconjunto: Crea una función que verifique si un conjunto es subconjunto de otro. 
def subconjunto(c1, c2):
    c3=c1.issubset(c2)
    return c3

conjunto1={1,2,3,4,5,6,7,8,9}
conjunto2={1,2,3,4,5,6,7,8,9,10,11,12,13,14}
conjunto3=subconjunto(conjunto1, conjunto2)
conjunto4=subconjunto(conjunto2,conjunto1)
if conjunto3 or conjunto4 == True:
    print("si es subconjunto")
else:
    print("no es subconjunto")
