'''
En un almacén se guarda mercadería en contenedores. No es posible colocar más de n contenedores uno encima 
del otro y, no hay área para más de 5 pilas de contenedores. Elabore un programa que permita gestionar el 
ingreso y salida de contenedores. Note que para retirar un contenedor es necesario retirar los contenedores 
que están encima de él y colocarlos en otra pila.
'''
# Inicialiciacion de variables:
pila_1 = ["Fideos", "Arroz", "Lentejas", "Arvejas", "Garbanzos"]
pila_2 = ["Atun",]
pila_3 = ["Palmitos",]
pila_4 = ["Choclo",]
pila_5 = ["Humita",]
almacen = [pila_1, pila_2, pila_3, pila_4, pila_5]

# Algoritmo:
print("Bienvenido al sistema de almacenamiento: ")
while True:
    # Almacen en pantalla: 
    contador = 0
    print("\nEl almacen se encuentra actualmente asi:")
    for pila in almacen:
          contador += 1
          print(f"Pila {contador}:")
          print(pila)
    
    accion = int(input("\nQue accion desea realizar?"
                    "\n1. Agregar contenedor."
                    "\n2. Retirar contenedor."
                    "\n3. Mover contenedores."
                    "\n0. Salir."))

    if accion == 0: # Salida del programa.
        print("\nFin del programa.")
        break
    elif accion == 1: # agregar contenedor.
        contenedor = input("\nIngrese un troquel a su contenedor: ")
        pila_almacen = int(input("En que pila desea almacenar su contenedor? (Ingrese valor entero entre 1 y 5) ")) - 1

        if len(almacen[pila_almacen]) > 4:
            print("\nNo queda espacio en esta pila.")
        else:
            almacen[pila_almacen].append(contenedor)
    elif accion == 2: # retirar contenedor.
        pila_almacen = int(input("Ingrese el numero de pila donde se encuentra el contenedor que desea retirar: "))
        contenedor = input("Ingrese exactamente el nombre del contenedor que desea retirar: ")

        if pila_almacen == 1:
           if contenedor == pila_1[len(pila_1) - 1]:
                print(f"Se retiro exitosamente el siguiente contenedor: {pila_1.pop(len(pila_1) - 1)}.")
           elif contenedor in pila_1:
                print("El contenedor se encuentra debajo, mueva los contenedores superiores primero.")
           else:
                print("No ingreso correctamente el troquel del contenedor.")
        elif pila_almacen == 2:
           if contenedor == pila_2[len(pila_2) - 1]:
                print(f"Se retiro exitosamente el siguiente contenedor: {pila_2.pop(len(pila_2) - 1)}.")
           elif contenedor in pila_2:
                print("El contenedor se encuentra debajo, mueva los contenedores superiores primero.")
           else:
                print("No ingreso correctamente el troquel del contenedor.")
        elif pila_almacen == 3:
           if contenedor == pila_3[len(pila_3) - 1]:
                print(f"Se retiro exitosamente el siguiente contenedor: {pila_3.pop(len(pila_3) - 1)}.")
           elif contenedor in pila_3:
                print("El contenedor se encuentra debajo, mueva los contenedores superiores primero.")
           else:
                print("No ingreso correctamente el troquel del contenedor.")
        elif pila_almacen == 4:
           if contenedor == pila_4[len(pila_4) - 1]:
                print(f"Se retiro exitosamente el siguiente contenedor: {pila_4.pop(len(pila_4) - 1)}.")
           elif contenedor in pila_4:
                print("El contenedor se encuentra debajo, mueva los contenedores superiores primero.")
           else:
                print("No ingreso correctamente el troquel del contenedor.")
        elif pila_almacen == 5:
           if contenedor == pila_5[len(pila_5) - 1]:
                print(f"Se retiro exitosamente el siguiente contenedor: {pila_5.pop(len(pila_5) - 1)}.")
           elif contenedor in pila_5:
                print("El contenedor se encuentra debajo, mueva los contenedores superiores primero.")
           else:
                print("No ingreso correctamente el troquel del contenedor.")
    elif accion == 3: # mover contenedor.
          pila_almacen = int(input("En que pila se encuentra el contenedor que desea mover? "))
          
          if pila_almacen == 1:
               contenedor = pila_1.pop(len(pila_1) - 1)
               mover_pila = int(input(f"Ud. tiene seleccionado el contenedor {contenedor}.\
                                        \nA que pila desea moverlo?\n"))
               
               if mover_pila == 2 and len(pila_2) < 5:
                    pila_2.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 2.")]
               elif mover_pila == 3 and len(pila_3) < 5:
                    pila_3.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 3.")]
               elif mover_pila == 4 and len(pila_4) < 5:
                    pila_4.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 4.")]
               elif mover_pila == 5 and len(pila_5) < 5:
                    pila_5.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 5.")]
               else:
                    pila_1.append(contenedor)
                    print("No has seleccionado una pila valida o esta pila esta llena.")
          elif pila_almacen == 2:
               contenedor = pila_2.pop(len(pila_2) - 1)
               mover_pila = int(input(f"Ud. tiene seleccionado el contenedor {contenedor}.\
                                        \nA que pila desea moverlo?\n"))
               
               if mover_pila == 1 and len(pila_1) < 5:
                    pila_1.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 1.")]
               elif mover_pila == 3 and len(pila_3) < 5:
                    pila_3.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 3.")]
               elif mover_pila == 4 and len(pila_4) < 5:
                    pila_4.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 4.")]
               elif mover_pila == 5 and len(pila_5) < 5:
                    pila_5.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 5.")]
               else:
                    pila_2.append(contenedor)
                    print("No has seleccionado una pila valida o esta pila esta llena.")
          elif pila_almacen == 3:
               contenedor = pila_3.pop(len(pila_3) - 1)
               mover_pila = int(input(f"Ud. tiene seleccionado el contenedor {contenedor}.\
                                        \nA que pila desea moverlo?\n"))
               
               if mover_pila == 1 and len(pila_1) < 5:
                    pila_1.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 1.")]
               elif mover_pila == 2 and len(pila_2) < 5:
                    pila_2.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 2.")]
               elif mover_pila == 4 and len(pila_4) < 5:
                    pila_4.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 4.")]
               elif mover_pila == 5 and len(pila_5) < 5:
                    pila_5.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 5.")]
               else:
                    pila_3.append(contenedor)
                    print("No has seleccionado una pila valida o esta pila esta llena.")
          elif pila_almacen == 4:
               contenedor = pila_4.pop(len(pila_4) - 1)
               mover_pila = int(input(f"Ud. tiene seleccionado el contenedor {contenedor}.\
                                        \nA que pila desea moverlo?\n"))
               
               if mover_pila == 1 and len(pila_1) < 5:
                    pila_1.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 1.")]
               elif mover_pila == 3 and len(pila_3) < 5:
                    pila_3.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 3.")]
               elif mover_pila == 2 and len(pila_2) < 5:
                    pila_2.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 2.")]
               elif mover_pila == 5 and len(pila_5) < 5:
                    pila_5.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 5.")]
               else:
                    pila_4.append(contenedor)
                    print("No has seleccionado una pila valida o esta pila esta llena.")
          elif pila_almacen == 5:
               contenedor = pila_5.pop(len(pila_5) - 1)
               mover_pila = int(input(f"Ud. tiene seleccionado el contenedor {contenedor}.\
                                        \nA que pila desea moverlo?\n"))
               
               if mover_pila == 1 and len(pila_1) < 5:
                    pila_1.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 1.")]
               elif mover_pila == 3 and len(pila_3) < 5:
                    pila_3.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 3.")]
               elif mover_pila == 4 and len(pila_4) < 5:
                    pila_4.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 4.")]
               elif mover_pila == 2 and len(pila_2) < 5:
                    pila_2.append(contenedor)
                    [print(f"Moviste exitosamente el contenedor {contenedor} a la PILA 2.")]
               else:
                    pila_5.append(contenedor)
                    print("No has seleccionado una pila valida o esta pila esta llena.")
     