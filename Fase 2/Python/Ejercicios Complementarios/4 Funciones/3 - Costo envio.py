'''
Un minorista en línea proporciona una forma de envío urgente de $ 10.95 para el primer elemento y $ 2.95 
para cada segundo elemento posterior. Escriba una función que tome el número de elementos en el pedido 
como su único parámetro. Devuelva los gastos de envío del pedido como resultado de la función. Incluya 
un programa principal que lea la cantidad de artículos comprados al usuario y muestre los gastos de envío.
'''
tarifa_fija = 10.95
extra = 2.95

costo_envio = lambda cantidad: (tarifa_fija - extra) + extra * cantidad

cantidad = int(input("Cuantos articulos desea enviar?: "))

print(f"Ud enviara {cantidad} articulos.\
    \nEl costo del envio es de ${costo_envio(cantidad):.2f}")