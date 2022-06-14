'''
En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo 
de un número que se escoge al azar. Si el numero escogido es menor que 74 el descuento es del 15% sobre 
el total de la compra, si es mayor o igual a 74 el descuento es del 20%. Obtener cuánto dinero se le descuenta.
'''
import random

ruleta = random.randint(1, 100)
descuento = 0

if ruleta < 74:
    descuento = 15
else: 
    descuento = 20

print(f"Su numero es el {ruleta}.\
    \n Felicitaciones!\
    \nUd. ha ganado un descuento del {descuento}%.")