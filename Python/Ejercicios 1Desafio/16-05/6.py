'''
6- 
Escribir un programa que pregunte el nombre el un producto, 
su precio y un número de unidades y muestre por pantalla una 
cadena con el nombre del producto seguido de su precio unitario 
con 6 dígitos enteros y 2 decimales, el número de unidades con 
tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

Solucion:


'''
Producto = input("Ingrese el nombre del producto: \n")
Precio = int(input("Ingrese el precio del producto: \n"))
Unidades = int(input("Ingrese el numero de unidades del producto: \n"))

CostoTotal = Precio * Unidades
#Precio = f'{(Precio):.2f}'
#CostoTotal = f'{(CostoTotal):.2f}'
#
#print(f"{Producto}  | $ {(Precio).zfill(9)}   | {Unidades:03d}\
#     |     $ {(CostoTotal).zfill(11)}")

print(f"{Producto}  | $ {(Precio):09.2f}   | {Unidades:03d}    | $ {(CostoTotal):011.2f}")