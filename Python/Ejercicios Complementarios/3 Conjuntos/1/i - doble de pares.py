'''
Elabore un programa que dada una lista de 15 elementos, copie en otra lista los elementos pares multiplicados por 2.
'''
import random


lista = [random.randrange(0,10) for num in range(15)]

lista_copia = [num * 2 for num in lista if (num % 2 == 0)]

print(lista)
print(lista_copia)