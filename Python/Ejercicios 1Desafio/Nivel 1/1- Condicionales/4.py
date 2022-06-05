'''
Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de 
receta aparecen a continuación.

Ingredientes comunes: Verduras y berenjena.
Ingredientes Receta 1: Lentejas y apio.
Ingredientes Receta 2: Morrón y Cebolla..

Escribir un programa que pregunte al usuario que tipo de receta desea, y en función 
de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) y el tipo 
de receta. Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes.
'''
'''
   --------------------------
  |      CON LISTAS         |
  --------------------------
Receta1 = ["lentejas", "apio"]
Receta2 = ["morron", "cebolla"]
Ingrediente1 = "verduras"
Ingrediente2 = "berenjena"

Eleccion = []

Eleccion.append(int(input(f"Elija entre los siguientes ingredientes para su plato: \
                    \n1. {Receta1[0].capitalize()} y {Receta1[1]}.\
                    \n2. {Receta2[0].capitalize()} y {Receta2[1]}.\n")))

Eleccion.append(int(input(f"Ademas puede agregar tambien:\
        \n1. {Ingrediente1.capitalize()}.\
        \n2. {Ingrediente2.capitalize()}.\n")))

if  Eleccion[0] == 1:
    if  Eleccion[1] == 1:
        print(f"Su plato contendra {Receta1[0]}, {Receta1[1]} y {Ingrediente1}. Buen provecho!")
    else:
        print(f"Su plato contendra {Receta1[0]}, {Receta1[1]} y {Ingrediente2}. Buen provecho!")

else:
    if Eleccion[1] == 1:
        print(f"Su plato contendra {Receta2[0]}, {Receta2[1]} y {Ingrediente1}. Buen provecho!")
    else:
        print(f"Su plato contendra {Receta2[0]}, {Receta2[1]} y {Ingrediente2}. Buen provecho!")
'''
#  --------------------------
# |      CON STRINGS        |
# --------------------------
Receta1 = "lentejas y apio"
Receta2 = "morron y cebolla"
Ingrediente1 = "verduras"
Ingrediente2 = "berenjena"

Eleccion = []

Eleccion.append(int(input(f"Elija entre los siguientes ingredientes para su plato: \
                    \n1. {Receta1.capitalize()}.\
                    \n2. {Receta2.capitalize()}.\n")))

Eleccion.append(int(input(f"Ademas puede agregar tambien:\
        \n1. {Ingrediente1.capitalize()}.\
        \n2. {Ingrediente2.capitalize()}.\n")))

if  Eleccion[0] == 1:
    if  Eleccion[1] == 1:
        print(f"Su plato contendra {Ingrediente1}, {Receta1}. Buen provecho!")
    else:
        print(f"Su plato contendra {Ingrediente2}, {Receta1}. Buen provecho!")

else:
    if Eleccion[1] == 1:
        print(f"Su plato contendra {Ingrediente1}, {Receta2}. Buen provecho!")
    else:
        print(f"Su plato contendra {Ingrediente2}, {Receta2}. Buen provecho!")
