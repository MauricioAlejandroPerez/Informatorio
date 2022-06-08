'''
Diseñar un programa que permita calcular el total de una compra, ingresando cantidad y precio de los productos. 
El programa debe estar preparado para que el ingreso de los datos se produzca hasta que el usuario lo desee.
'''
# Iniciando variables:
carrito = 0

# Algoritmo:
print("Bienvenidos al sistema de compras")
while True:
    # Condicion de ingreso y cierre:
    cc = input("Para cargar un producto presione 'Enter'.\
            \nSi desea finaliazar inserte 'fin'.\n").lower()
    if cc == "fin":
        break
    elif cc != "":
        print("El valor ingresado es incorrecto, intente nuevamente.\n\n")
        continue
    
    # Almacenamiento de las compras:
    unidades_compradas = int(input("Ingrese la cantidad de unidades que compro: "))
    precio_producto = float(input("Ingrese el precio del producto: "))
    monto_cargado = (unidades_compradas * precio_producto)
    carrito += monto_cargado
        # Recuento en pantalla:    
    print(f"\nUd. agrego una compra por $ {monto_cargado:.2f}.\
        \nEl total de la compra asciende a $ {carrito:.2f}.\n")    

# Resultado:
print(f"\nCompra finalizada. El total a pagar es $ {carrito:.2f}.\n")