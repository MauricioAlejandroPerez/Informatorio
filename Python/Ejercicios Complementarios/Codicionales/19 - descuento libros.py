'''
print('Bienvenido al sistema de bonificaciones. \n Ingrese L para tipo de clientes Librerías y P para tipo de clientes Particular')
tipocliente = input("Ingrese tipo de Cliente para comenzar a operar:\n").upper()
cantidadcompra = int(input("Ingrese la cantidad comprada:\n"))
importetotal = float(input("Ingrese el importe total de la compra: \n"))

if tipocliente=='L':
    if cantidadcompra<=24:
        importebonificado = importetotal - (importetotal * 0.2)   #importebonificado = importetotal * 0.8
    else:
        importebonificado = importetotal - (importetotal * 0.25)  #importebonificado = importetotal * 0.75
    print(f"El importe a cobrar con bonificación es de :{importebonificado}, para {cantidadcompra} elementos comprados y tipo de cliente {tipocliente}")

elif tipocliente=='P':
    if cantidadcompra>18:
        importebonificado = importetotal - (importetotal * 0.1)
    elif cantidadcompra>=6 and cantidadcompra<=18:
        importebonificado = importetotal - (importetotal * 0.05)
    else:
        importebonificado = importetotal
    print(f"El importe a cobrar con bonificación es de :{importebonificado}, para {cantidadcompra} elementos comprados y tipo de cliente {tipocliente}")
else:
    print("La letra ingresada para tipo de cliente es incorrecta.\n Ingrese 'L' para Librerías y 'P' para Particular.")


'''

'''
Una distribuidora de libros vende a librerías y a particulares. Aplica bonificaciones por 
cantidad según el siguiente criterio:

i.      a librerías: hasta 24 unidades, el 20%; más de 24 unidades, el 25%.

ii.      a particulares: menos de 6 unidades, nada; desde 6 hasta 18 unidades, el 5% y más de 18 unidades, el 10%.

El tipo de cliente está codificado así: 'L' para librerías, 'P' para particular. Dado el importe bruto de una compra 
de libros, el tipo de cliente de que se trata y la cantidad total pedida por el mismo, determinar el importe bruto 
bonificado.
'''
tipo_comprador = input("Ingrese el tipo de cliente:\
                    \nPara librerias ingrese 'L'.\
                    \nPara particulares ingrese 'P'.\n").lower()
unidades_compradas = int(input("Ingrese la cantidad de unidades que compro el cliente:\n"))
monto_total = float(input("Ingrese el monto total de la compra:\n"))
descuento = 0

if tipo_comprador == "l":
    if unidades_compradas <= 24:
        descuento = 20
    elif unidades_compradas > 24:
        descuento = 25
elif tipo_comprador == "p":
    if unidades_compradas > 6 and unidades_compradas <= 18:
        descuento = 5
    elif unidades_compradas > 18:
        descunto = 10
monto_a_pagar = monto_total * (1 - descuento/100)

print(f"El pedido por {unidades_compradas} libros asciende a un total de ${monto_total:.2f}.")
if descuento != 0:
    print(f"Por su compra obtiene un descuento del {descuento}%.\
        \nEl monto a abonar es ${monto_a_pagar:.2f}.")