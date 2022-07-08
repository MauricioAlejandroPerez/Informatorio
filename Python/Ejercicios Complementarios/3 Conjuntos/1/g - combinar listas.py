'''
Cargar dos listas con la misma cantidad de elementos. Luego mezclarlas, cargándolas ordenadas en otra lista.
'''
import random


lista_1 = [random.randrange(1, 6) for num in range(3)]
lista_2 = [random.randrange(6, 11) for num in range(3)]

print(lista_1)
print(lista_2)


lista_comb1 = lista_1 + lista_2
lista_comb2 = [*lista_1, *lista_2]

print(lista_comb1)
print(lista_comb2)

lista_1.pop()

print(lista_1)
print(lista_2)
print(lista_comb1)
print(lista_comb2)