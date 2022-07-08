'''
Cargar k elementos en una cola, y luego copiarlos en una nueva lista.
'''
# cola: FIFO, first in, fisrt out
lista_cola = []
contador = 0

print("A continuacion ingrese 5 numeros enteros: ")
while contador < 5:
    contador += 1
    lista_cola.append(int(input(f"Ingrese el {contador}* numero: ")))

lista_copia = lista_cola.copy()

print(lista_cola)
print(lista_copia)