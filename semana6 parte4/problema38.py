 #Registro de Estudiantes con Notas y Asignaturas: Diseña un programa que permita 
 # ingresar información sobre varios estudiantes. Cada estudiante tiene un nombre, 
 # un diccionario de asignaturas (donde las claves son los nombres de las asignaturas 
 # y los valores son las calificaciones), y una lista de amigos (nombres de otros estudiantes). 
alumnos={}
num=int(input("ingrese el numero de estudiantes"))
for i in range(num):
    asignatura={}
    lista=[]
    dic={}
    nom=input("ingrese el nombre del estudiante ")
    asi=int(input("ingrese el numero de asignaturas "))
    for j in range(asi):
        asig=input("ingrese el nombre de la asignatura ")
        cal=int(input("ingrese su claificacion en la asignatura "))
        asignatura[asig]=cal
    ami=int(input("ingrese el numero de amigos "))
    for k in range(ami):
        amig=input("ingrese el nombre del amigo ")
        lista.append(amig)
    dic["amigos"]=lista
    dic["asignaturas"]=asignatura
    alumnos[nom]=dic




