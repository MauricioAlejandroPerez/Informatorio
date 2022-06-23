'''
b. 	Haz un programa que almacene 5 elementos en una variable del tipo lista, la modiﬁque para que cada 
componente sea igual al cuadrado del componente original. El programa mostrara la lista resultante por 
pantalla.
'''
# Variables a utilizar:
count = 0
lista = []

# Ingreso de los elementos de la lista:
print("A continuacion ingrese 5 numeros enteros: ")
while count < 5:
    count += 1
    lista.append(int(input(f"Ingrese el {count}* numero: ")))

# Lista de cuadrados
cuadrados = [num**2 for num in lista ]

#Resultado por pantalla:
print(cuadrados)