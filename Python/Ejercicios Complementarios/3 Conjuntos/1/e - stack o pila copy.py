'''
Cargar m elementos en una pila, y luego copiarlos en una nueva lista.
'''
# pila: LIFO, ultima entrada, primero salida
lista_pila = []
contador = 0

print("A continuacion ingrese 5 numeros enteros: ")
while contador < 5:
    contador += 1
    lista_pila.insert(0, int(input(f"Ingrese el {contador}* numero: ")))

lista_copia = lista_pila.copy()

print(lista_pila)
print(lista_copia)