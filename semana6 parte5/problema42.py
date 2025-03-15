#Diccionario de Países con Información Geográfica: Crea un diccionario que relacione países 
# con su información geográfica. Cada país tiene un nombre, una lista de ciudades importantes
#  y una lista de coordenadas (diccionarios con claves “latitud” y “longitud”). 
paises = {}

num_paises = int(input("ingrese la cantidad de países: "))

for i in range(num_paises):
    pais = {} 
    ciudades = []
    coordenadas = []

    nom_pais = input(f"ingrese el nombre del país {i+1}: ").capitalize()
    num_ciu = int(input("ingrese la cantidad de ciudades importantes: "))
    for j in range(num_ciu):
        ciudad = input(f"ingrese el nombre de la ciudad {j+1}: ").capitalize()
        latitud = float(input(f"ingrese la latitud de {ciudad}: "))
        longitud = float(input(f"ingrese la longitud de {ciudad}: "))
        ciudades.append(ciudad)
        coordenadas.append({"latitud": latitud, "longitud": longitud})

    pais["ciudades importantes"] = ciudades
    pais["coordenadas"] = coordenadas
    paises[nom_pais] = pais
