'''
Hacer un programa que imprima el nombre de un artículo, clave, precio original y su precio con descuento. 
El descuento lo hace en base a la clave, si la clave es 01 el descuento es del 10% y si la clave es 02 el 
descuento en del 20% (solo existen dos claves).
'''
articulo = input("Ingrese el nombre del articulo:\n")
clave = input("Ingrese clave de descuento:\
            \n01. Descuento del 10%.\
            \n02. Descuento del 20%.")
precio = float(input("Ingrese el precio del articulo:\n"))
precio_descontado = 0

if clave == "01": 
    precio_descontado = precio * .9 
elif clave == "02":
    precio_descontado = precio * .8 

print(f"Articulo:\t{articulo}\
    \nPrecio:\t${precio:.2f}\
    \nClave:\t{clave}\
    \nPrecio con Descuento:\t${precio_descontado:.2f}")

