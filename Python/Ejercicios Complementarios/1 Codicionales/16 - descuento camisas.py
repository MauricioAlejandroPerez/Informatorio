'''
Hacer un programa que calcule el total a pagar por la compra de camisas. Si se compran tres 
camisas o mas se aplica un descuento del 20% sobre el total de la compra y si son menos de 
tres camisas un descuento del 10%.
'''
monto_total = float(input("Ingrese el monto total de la compra:\n"))
cantidad_camisas = int(input("Ingrese la cantidad de camisas compradas:\n"))

if cantidad_camisas >= 3:
    descuento = .2
    monto_a_pagar = monto_total * (1-descuento)
elif cantidad_camisas < 3:
    descuento = .1
    monto_a_pagar = monto_total * (1-descuento)

print(f"Ud. esta llevando {cantidad_camisas} camisas por un total de ${monto_total:.2f}.\
    \nPor su compra obtiene un descuento del {(descuento * 100):.0f}%.\
    \nEl monto a abonar es ${monto_a_pagar:.2f}.")
