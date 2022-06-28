'''
Realice una función que dada una lista de enteros L, y un número entero n. Elimine de la lista 
original los elementos que sean iguales a ese número dado.
'''
import random

lista = [random.randrange(1,5) for x in range(10)]

print(lista)

valor = int(input("Ingrese un valor entre 1 y 10 que desee quitar de la lista: "))

lista[:] = (value for value in lista if value != valor)

print(lista, type(lista))

# new_list = []
# 
# for elemento in lista:
    # if elemento != valor:
        # new_list.append(elemento)

# print(new_list)


