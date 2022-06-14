'''
Calcular el monto a pagar por cada cliente y total recaudado en una estación de servicio. 
Debe diseñar un programa que permita monto por cliente y el total recaudado por la gasolinera, 
tomando en cuenta lo siguiente:

• El precio del litro es para el Tipo A $50, para el Tipo B $ 55 y para el Tipo C $60

• El programa finaliza cuando se introduce una D como tipo de gasolina.
'''
precio = 0
nafta_gasoil = 0
nafta_super = 0
nafta_premium = 0
recaudacion = 0

print("Bienvenidos al software 1.0b de surtidores.")
while True:
    # Determina el tipode combustible a cargar:
    tipo_nafta = input("Que combustible desea cargar?:\
                        \nA. Gasoil.\
                        \nB. Super.\
                        \nC. Premium.\
                        \nD. Salir del programa.\n").lower()

    if tipo_nafta == "d":
        break

    # Monto de la carga
    elif tipo_nafta == "a" or tipo_nafta == "b" or tipo_nafta == "c": 
        cantidad = float(input("Que monto de combustible desea cargar?\n"))
        recaudacion += cantidad
        if tipo_nafta == "a":
            nafta = "GASOIL"
            precio = 50
            carga = cantidad / precio
            nafta_gasoil += cantidad
        elif tipo_nafta == "b":
            nafta = "SUPER"
            precio = 55
            carga = cantidad / precio
            nafta_super += cantidad
        elif tipo_nafta == "c":
            nafta = "PREMIUM"
            precio = 60
            carga = cantidad / precio
            nafta_premium += cantidad
        # Fin de cada carga:
        print(f"\nSe cargaron {carga:.2f} lts. de nafta {nafta}, por un monto de ${cantidad:.2f}")
        print("\nIngrese un nueva carga.")
    else:
        print("\nEl valor ingresado no es correcto\n")
        continue

# Resultado por pantalla al finalizar el programa:
print(f"Muchas gracias por usar el software de surtidores.\
    \nEl total recaudado el dia de hoy es ${recaudacion:.2f}.\
    \n\tTotal nafta GASOIL: ${nafta_gasoil:.2f}.\
    \n\tTotal nafta SUPER: ${nafta_super:.2f}.\
    \n\tTotal nafta PREMIUM: ${nafta_premium:.2f}.")