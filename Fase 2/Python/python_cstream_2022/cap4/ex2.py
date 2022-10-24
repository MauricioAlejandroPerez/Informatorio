import random

lista = []
for x in range (0,10):
    lista.append (random.randint(0,100))

print(lista)

for x in range(0, len(lista)):
    msg = f"iteracion {x}: lista[{x}] = lista[{x}] * 2  :: {lista[x]} * 2"
    print(msg)
    lista[x] = lista[x] * 2

print(lista)