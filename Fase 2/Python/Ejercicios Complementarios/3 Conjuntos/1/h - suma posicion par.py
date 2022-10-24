'''
Construya un algoritmo que sume todos los elementos en posición par de una lista.
'''
import random


lista = [random.randrange(0,10) for num in range(10)]
suma_pos_par = 0

for position, elemento in enumerate(lista):
    if position % 2 == 0:
        suma_pos_par += elemento

print(lista)
print(suma_pos_par)