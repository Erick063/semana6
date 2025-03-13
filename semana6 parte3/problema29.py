#Diccionario de Sinónimos: Crea un diccionario que contenga palabras y sus sinónimos. 
# El usuario debe poder buscar sinónimos para una palabra dada. 
# Al finalizar, imprime solo las claves del diccionario. 
sinonimos = {
    "feliz": ["contento", "alegre", "satisfecho"],
    "rápido": ["veloz", "ligeiro", "acelerado"],
    "inteligente": ["listo", "sabio", "astuto"],
    "fuerte": ["robusto", "poderoso", "resistente"]
}

p = input("ingrese la palabra que quiere buscar sinonimos ").lower()
if p in sinonimos:
    print(f"sinónimos de '{p}': {', '.join(sinonimos[p])}")
else:
    print("no se encontraron sinónimos para ", p)
print("las palabras con sinonimos son ")
for i in sinonimos.keys():
    print(i)
