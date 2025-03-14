#Diccionario de Notas de Estudiantes: Diseña un programa que permita ingresar las notas de 
# varios estudiantes. Cada estudiante tiene un nombre y una lista de calificaciones. 
# Utiliza un diccionario para almacenar esta información. 
calificaciones={}
num=int(input("ingrese el numero de estudiantes "))
for i in range(num):
    lista=[]
    nom=input("ingrese el nombre del estudiante ")
    numcali=int(input("ingrese el numero de calificaciones del estudiante "))
    for j in range(numcali):
        cali=int(input(f"ingrese la calificacion {j+1} del estudiante "))
        lista.append(cali)
    calificaciones[nom]=lista