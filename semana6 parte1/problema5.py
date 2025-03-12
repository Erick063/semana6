#Cifrado César Personalizado: Implementa una función que tome una cadena y un desplazamiento (número entero).
# Realiza un cifrado César en la cadena, desplazando cada letra según el valor dado.
# Asegúrate de manejar correctamente los límites del alfabeto (por ejemplo, si llegas a ‘z’, debes volver a ‘a’). 
def cesar(txt,n):
    abc="abcdefghijklmnopqrstuvwxyz"
    new=""
    for i in txt:
        if i.isalpha():
            index = abc.index(i.lower())
            n_i = (index + n) % len(abc)
            if i.islower():
                new += abc[n_i]
            else:
                new +=abc[n_i].upper()
        else:
            new += i
    return new


txt=input("ingrese un texto: ")
n=int(input("ingrese el numero de pasos que dar: "))
pal=cesar(txt,n)

print(pal)
