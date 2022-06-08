''''
Hacer un programa que permita determinar todos los divisores de un número ingresado por el teclado.
'''
divisores = ""
numero = int(input("Ingrese un numero entero para conocer todos sus divisores: "))
count = numero

for num in range(numero, 0, -1):
    if numero % num == 0:
        divisores += str(num) + ", "
    count -= 1
    if count == 0:
        divisores = divisores.strip(", ")
        divisores = divisores + "."

print(divisores)
