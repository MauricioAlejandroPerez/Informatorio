'''
7- 
Escribir un programa que pregunte por consola por los productos 
de una cesta de la compra, separados por comas, y muestre por 
pantalla cada uno de los productos en una línea distinta

'''

ListaDeCompra = input("Ingrese los productos que desee separados por una ', ': \n" ).split(", ")

print(*ListaDeCompra, sep = "\n")