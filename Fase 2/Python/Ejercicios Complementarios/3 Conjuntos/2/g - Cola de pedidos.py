'''
Se tiene una lista que almacena pedidos en orden de llegada, por ende puede haber más de un pedido 
para el mismo artículo. Crear una lista donde se almacene la cantidad de pedidos por artículo.
'''
cola_de_pedidos = []
articulos = ["Mate", "Cafe", "Harina", "Palmitos", "Yerba", "Mermelada", "Cacao", "Picadillo"]
# 
pedidos_por_articulo = {}
for articulo in articulos:
    pedidos_por_articulo[articulo] = 0

print("Bienvenido al sistema de pedidos Marolio.")
while True:
    funciones = int(input("\nSeleccione una opcion:\
                        \n1. Ver catalogo.\
                        \n2. Cargar producto al pedido.\
                        \n3. Informe de pedidos por articulos.\
                        \n4. Cola de pedidos.\
                        \n0. Para salir del programa."))

    if funciones == 0: # Salida del programa.
        break
    elif funciones == 1: # Muestra del catalogo.
        
        print("Catalogo de Productos: ")
        print("|Codigo|\t|Articulo|")
        cont_art = 0
        for articulo in articulos:
            cont_art += 1
            print(f"|{cont_art}|\t\t{articulo}")
        continue
    elif funciones == 2: # Toma de pedidos.
        # Toma del pedido:
        pedido = []
        while True:
            carga = int(input("Ingrese el codigo del producto que desea cargar (0 para finalizar): "))
            if carga == 0:
                break
            elif carga > 0 and carga < len(articulos):
                pedido.append(articulos[carga-1])
            else:
                print("Codigo incorrecto, intente nuevamente.")
        print(f"Su pedido es: {pedido}")
        # Carga al informe.
        for articulo in pedido:
            pedidos_por_articulo[articulo] += 1
        # Carga a la cola de pedidos.
        cola_de_pedidos.append(pedido)
    elif funciones == 3: # Informe de perdidos por articulos.
        print("\nInforme acercad de los pedidos:")
        for articulo in pedidos_por_articulo:
            print(f"{articulo}: {pedidos_por_articulo[articulo]}")
    elif funciones == 4: # Cola de pedidos.
        print("\nCola de pedidos:")
        print("|Posicion|\t|Pedido|")
        cont_qeue = 0
        for pos, ped in enumerate(cola_de_pedidos):
            cont_qeue += 1
            print(f"  {pos}.\t\t{ped}")

    else: # Valor no valido.
        print("\nLa opcion ingresada no corresponde a ninguna funcion.\
                \nVuelva a intentarlo.")
