#Registro de Temperaturas Diarias: Diseña un programa que permita al usuario ingresar las 
# temperaturas diarias de una semana. Cada día se representa como una tupla (día, temperatura).
#  Luego, muestra la temperatura promedio de la semana. 
dic={}
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
suma=0
for i in dias:
    tem=int(input(f"ingrese la temperatura del dia {i} "))
    suma+=tem
    n = (i, tem) 
print("la temperatura promedio es de ", suma/7)
