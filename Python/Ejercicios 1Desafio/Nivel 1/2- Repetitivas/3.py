'''
En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra llegan 
a la caja y ofrecen tapitas para reciclar, de acuerdo a la cantidad que lleven en la caja le entregan 
un código de descuento que se aplicará sobre el total de su compra. Determinar la cantidad que pagara 
cada cliente desde que la tienda abre hasta que cierra. 

Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; si es amarilla un 25% 
y si es blanca no obtendrá descuento.
'''
# Tarjetas de descuento:
rojo = .4
amarillo = .25
blanco = 0

# Algoritmo de cobro:
while input("Para realizar una nueva compra presione 'Enter'") == "":
    monto_a_pagar = float(input("Ingrese el total de la compra: \n"))
    codigo = int(input("Posee un codigo de descuento? \
                    \n1. Blanco.\
                    \n2. Amarillo.\
                    \n3. Rojo.\n"))
    if codigo == 1:
            print(f"El monoto a pagar es: ${monto_a_pagar:.2f}")
    elif codigo == 2:
            print(f"El monoto a pagar es: ${((monto_a_pagar) * (1-amarillo)):.2f}")
    elif codigo == 3:
            print(f"El monoto a pagar es: ${((monto_a_pagar) * (1-rojo)):.2f}")
    
    print("Gracias por su compra!")