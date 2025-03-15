#Diccionario de Películas con Géneros y Actores: Diseña un programa que almacene 
# información sobre películas. Cada película tiene un nombre, una lista de géneros
# (como “acción”, “comedia”, etc.) y una lista de actores principales. 
pelicula={}
num=int(input("ingrese la cantidad de peliculas que va almacenar informcacion "))
for i in range(num):
    dic={}
    generos=set()
    actores=set()

    nombre=input(f"ingrese el nombre de la pelicula {i+1} ")
    num_gen=int(input("ingrese la cantidad de generos que tiene "))
    for j in range(num_gen):
        gen=input("ingrese el genero ").capitalize()
        generos.add(gen)

    num_act=int(input("ingrese la cantidad de actores principales "))
    for k in range(num_act):
        gen=input("ingrese el actor ").capitalize()
        actores.add(gen)

    lis_gen=list(generos)
    lis_act=list(actores)
    dic["lista de generos"]=lis_gen
    dic["lista de actores"]=lis_act
    pelicula[nombre]=dic





