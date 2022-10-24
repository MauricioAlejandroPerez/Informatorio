# Generar dos listas de 100 numeros random y luego crear una tercer lista con los numeros que coinciden. Si ninguno de los numeros coinciden, la lista final es vacia.
# Mostrar la lista 1
# Mostrar la lista 2
# Mostrar la lista 3 de coincidentes e imprimir un mensaje diciendo cuantos coincidentes hay

import random

lista1 = []
lista2 = []
resultado = set()

for i in range(0,100):
    lista1.append(random.randint(0,1000))
    lista2.append(random.randint(0,1000))

for i in lista1:
    if i in lista2:
        resultado.add(i)


print(f"lista 1: -  {lista1} \n")
print(f"lista 2: -  {lista2} \n")
print(f"resultado: -  {resultado}")
print(f"Coincidentes: {len(resultado)}")