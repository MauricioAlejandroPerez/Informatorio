'''
Escriba un algoritmo que permita cargar una lista. Y que luego, una vez cargada, controle 
y sustituya cualquier elemento negativo por 0.
'''
import random

# for i in range(10):
#     lista_random.append(random.randint(-100, 100))
#
# for i in lista_random:
    # if i < 0:
        # lista_random[lista_random.index(i)] = 0

lista_random = [random.randrange(-100, 100) for value in range(10)]

print(lista_random)

lista_random = [elementos if elementos > 0 else 0 for elementos in lista_random]

print(lista_random)