#Registro de Alumnos: Diseña un programa que permita al usuario ingresar información sobre 
# varios alumnos (nombre, edad, calificaciones, etc.). Cada alumno se representará como una 
# tupla. Luego, muestra la lista de alumnos y sus datos. 

lista_alumnos={}
num=int(input("ingrese el numero de estudiantes "))
for i in range(num):
    datos=[]
    lista=[]
    nom=input("ingrese el nombre del estudiante ")
    edad=input("ingrese la edad del estudiante ")
    matricula=int(input("ingrese la matricula del estudiante "))
    numcali=int(input("ingrese el numero de calificaciones del estudiante "))
    for j in range(numcali):
        cali=int(input(f"ingrese la calificacion {j+1} del estudiante "))
        lista.append(cali)
    datos.append(edad)
    datos.append(matricula)
    datos.append(lista)


    lista_alumnos[nom]=tuple(datos)
print(lista_alumnos)
                              