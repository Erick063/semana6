#Matriz de Coordenadas Polares: Escribe un programa que tome una coordenada polar almacenada en una 
# tupla (r, θ)). Convierte esa coordenada a coordenadas cartesianas (x, y) y muestra la tupla resultante. 
import math

def conversion(c_p):
    r, angulo = c_p 
    x = r * math.cos(math.radians(angulo))
    y = r * math.sin(math.radians(angulo))
    return (x, y)

r = float(input("ingrese el valor del radio: "))
angulo = float(input("ingrese el valor del ángulo en grados: "))

c_p = (r, angulo)

cartesiano = conversion(c_p)

print(f"la coordenada cartesiana es: {cartesiano}")
