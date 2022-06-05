'''
Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. Obtenga para 
determinado cliente cuánto deberá pagar finalmente por su compra y el descuento obtenido, si es que corresponde.
'''
monto_compra = int(input("Ingresar el monto a abonar:\n"))
descuento = .15

if monto_compra < 1000:
    print(f"El total a abonar ${monto_compra:.2f}")
else:
    print(f"El monto de las compra es de ${monto_compra}.\
          \nObtuvo un descuento de ${(monto_compra*descuento):.2f}\
          \nEl total a abonar ${(monto_compra * (1 - descuento)):.2f}.")