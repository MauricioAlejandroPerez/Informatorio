'''
Una pizzería, vende sus pizzas en tres tamaños: pequeña, mediana; y grandes. Una pizza puede ser sencilla 
(con sólo salsa y carne), o con ingredientes extras, tales como pepinillos, champiñones o cebollas. 
Desarrolle una solución que calcule el precio de venta de una pizza, dándole el tamaño y el número de 
ingredientes extras. El precio de venta será 1.5veces el costo total, que viene determinado por el tamaño, 
más el número de ingredientes. En particular el costo total se calcula sumando:

- un costo fijo de preparación.

- un costo variable que es proporcional al tamaño de la pizza.

- un costo adicional por cada ingrediente extra (por simplicidad se supone que cada ingrediente extra tiene el mismo costo).
'''
cf_pizza = 50
pizza_s = 50
pizza_m = 75
pizza_l = 100
precio_topping = 25
toppings = 0
cv = 0

valor_error = "\nValor ingresado incorrecto.\nIntente nuevamente."

# Programa:
print("Bienvenido al servicio de delivery.")
while True:
    costo = cf_pizza
    # Ingreso o condiccion de cierre:
    ingreso = input("\nDesea encargar una pizza? (S/N): ").lower()
    if ingreso == "s":
        tamanio = int(input("De que tamanio desea su pizza?:\
                \n1. Pequenia.\
                \n2. Mediana.\
                \n3. Grande.\
                \n4. Salir del programa."))
        if tamanio == 1:
            costo += pizza_s
        elif tamanio == 2:
            costo += pizza_m
        elif tamanio == 3:
            costo += pizza_l
        elif tamanio == 4:
            break
        else:
            print(valor_error)
            continue
    elif ingreso == "n":
        break
    else:
        print(valor_error)
        continue

    # Toppings:
    cant_toppings = 0

    while True:
        toppings = int(input("Desea agregar otro topping?:\
                        \n1. Pepinillo.\
                        \n2. Champignones.\
                        \n3. Cebolla.\
                        \n4. No, gracias."))

        if  toppings == 1 or toppings == 2 or toppings == 3:
            cant_toppings += 1
        elif toppings == 4:
            break
        else:
            print(valor_error)
            continue
    
    # Costo de la pizza:
    costo += cant_toppings * precio_topping
    print(costo)

    # Precio de la pizza (resultado en pantalla):
    print(f"\nSu pedido cuesta $ {(costo * 1.5)}. Muchas gracias por su compra.")