'''
Realizar un algoritmo que invierta el orden de una cola.
'''
lista_cola = []
contador = 0

print("A continuacion ingrese 5 numeros enteros: ")
while contador < 5:
    contador += 1
    lista_cola.append(int(input(f"Ingrese el {contador}* numero: ")))

print(lista_cola)

lista_cola = lista_cola[::-1]

print(lista_cola)