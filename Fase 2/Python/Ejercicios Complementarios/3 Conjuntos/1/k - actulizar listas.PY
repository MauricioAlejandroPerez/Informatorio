'''
Cargue dos listas, y actualice la primer lista con los elementos que están en la segunda y no en la primera.
'''
lista_1 = list(range(1, 8))
lista_2 = list(range(4, 10))

print(lista_1)
print(lista_2)

lista_1[len(lista_1):] = [num for num in lista_2 if num not in lista_1]

print(lista_1)
