'''
Diseñar un programa que permita obtener el producto entre A y B mediante sumas sucesivas.
'''
a = int(input("Ingrese el primer valor:\n"))
b = int(input("Ingrese el segundo valor:\n"))
producto = 0
count = 0

while count < b:
    count += 1
    producto += a
 
print(f"El producto de 'A = {a}' por 'B = {b}' es igual a {producto}.")
