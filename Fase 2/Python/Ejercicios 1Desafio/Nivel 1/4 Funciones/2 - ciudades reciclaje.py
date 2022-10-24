'''
Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades 
se cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.

Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.

Si ambos números son iguales, debe devolver el nombre de ambas.
'''
# Variables:
ciudades = {
    "Buenos Aires": 500,
    "Mendoza": 233,
    "Santa Fe": 300,
    "Cordoba": 500
}
contador = 0
ciudad = {}

# Funciones
def relacion (a, b):
    if ciudades[ciudad[a]] > ciudades[ciudad[b]]:
        print(f"La ciudad de {ciudad[a]} recicla una mayor cantidad de toneladas de basura.")
    elif ciudades[ciudad[a]] < ciudades[ciudad[b]]:
        print(f"La ciudad de {ciudad[b]} recicla una mayor cantidad de toneladas de basura.")
    elif ciudades[ciudad[a]] == ciudades[ciudad[b]]:
        print(f"Ambas ciudades reciclan la misma cantidad de toneladas de basura.")

# Algoritmo
print("Comparativa entre toneladas recicladas por ciudad:")
for k, v in ciudades.items():
    contador += 1
    print(f"{contador}. {k}.")
    ciudad[contador] = k

a = int(input("Ingrese la primer ciudad a comparar: "))
b = int(input("Ingrese la segunda ciudad a comparar: "))

relacion(a, b)