# Generar una lista de 10 numeros aleatorios y mostrar solamente
# aquellos que son pares

import random
lista = []

for x in range(0,10):
    lista.append(random.randint(0,100))

print(lista)

for num in lista:
    if ( (num % 2) == 0 ):
        print(f"{num} es par")
