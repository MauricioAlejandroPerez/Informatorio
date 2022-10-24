'''
En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un 
número que se escoge al azar. Si el número escogido es menor que 50 el descuento es del 15% sobre el total de 
la compra, si es mayor o igual a 50 el descuento es del 20%. Obtener cuánto dinero se le descuenta.
'''
import random

valor_error = "\nValor ingresado incorrecto.\nIntente nuevamente."

print("Bienvenido al sistema de compras e-market.")
while True:
    # Ingreso/Condicion de cierre:
    cc = input("\nDesea realizar una compra: (S/N): ")

    if cc == "n":
        break
    elif cc != "s":
        print(valor_error)
        continue

    
    # Ruleta:
    print("En nuestro comercio puede ganar descuentos mediante un sistema de ruleta.")
    
    ruleta = random.randint(1, 100)
    descuento = 0
    if ruleta < 50:
        descuento = 15
    else: 
        descuento = 20
    print(f"Su numero es el {ruleta}.\
    \nFelicitaciones! Ud. ha ganado un descuento del {descuento}%.")
    # Compra:
    monto_compra = float(input("Ingrese el monto total de su compra: "))
    
    

    # Resultado:
    print(f"\nEl total de su compra es de ${monto_compra:.2f} y recibira un descuento por ${(monto_compra * (descuento/100)):.2f}.\
    \nEl monto a pagar es ${(monto_compra * (1 - descuento / 100)):.2f}.\
    \nMuchas gracias por su compra, esperamos volver a verlo pronto!")