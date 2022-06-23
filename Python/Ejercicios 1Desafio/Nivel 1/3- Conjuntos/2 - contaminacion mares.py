'''
Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y niñas, 
aprendiendo sobre contaminación del agua crea un programa que pida números, si el numero esta entre 
1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.

El programa termina cuando el usuario introduce un cero.
'''
# Variables:
factores_contaminacion = ("\nError. El numero ingresado no es correcto, intentelo nuevamente.",

                            "\n1) Las aguas residuales: Proceden principalmente de los hogares, los comercios y la industria."
                            " Antes de ser vertidas al mar son tratadas para eliminar los mayores contaminantes, pero "
                            "no suele ser suficiente para depurarlas por completo.",

                            "\n2) Las sustancias químicas tóxicas: Es la principal causa de contaminación de los océanos. "
                            "Las sustancias químicas provienen en su mayoría de las actividades industriales y afectan "
                            "directamente a la salud de los seres marinos y terrestres.",
                            
                            "\n3) Las aguas pluviales: Son las utilizadas en las zonas de cultivo y por lo general suelen "
                            "contener herbicidas, plaguicidas y fertilizantes que terminarán por filtrarse a las aguas "
                            "subterráneas y a los ríos para finalmente terminar en el mar.",
                            
                            "\n4) El vertido de plásticos: Los plásticos pueden llegar a tardar en degradarse entre los 150 y"
                            " los 1000 años. Todos los residuos de plásticos vertidos al mar afectan directamente a la "
                            "fauna marina, ya que confunden estos desechos con comida o se quedan atrapados.",
                            
                            "\n5) Los vertidos de petróleo: Por norma general estos vertidos suelen ser accidentes, pero esto "
                            "no resta el daño que provoca a los seres vivos de la zona.",
                            
                            "6) La actividad minera en alta mar: Provoca contaminación acústica en el mar perjudicando a las "
                            "especies más sensibles a las ondas acústicas, ya que pueden llegar a confundirlas y "
                            "desorientarse.",
                            
                            "\n7) El cambio climático: No es un factor contaminante directamente, pero si influye en el océano."
                            " El aumento de las temperaturas provoca el descongelamiento de los polos, el aumento del nivel"
                            " del mar y de su temperatura, modifica las rutas migratorias de las especies y puede llegar a "
                            "acidificarlo.")

# Algoritmo:
print("Bienvenido al programa de concientizacion sobre la contaminacion de los mares.")
while True:
    
    cc = int(input("\nIngrese un numero del 1 al 7 para conocerlos principales motivos de contaminacion."
                    "\n(Ingrese 0 para salir)\n"))

    if cc == 0:
        print("Muchas gracias por su compromiso con el cuidado del planeta, cuidemoslo entre todos.")
        break
    elif cc == 1:
        print(factores_contaminacion[1])
        continue
    elif cc == 2:
        print(factores_contaminacion[2])
        continue
    elif cc == 3:
        print(factores_contaminacion[3])
        continue
    elif cc == 4:
        print(factores_contaminacion[4])
        continue
    elif cc == 5:
        print(factores_contaminacion[5])
        continue
    elif cc == 6:
        print(factores_contaminacion[6])
        continue
    elif cc == 7:
        print(factores_contaminacion[7])
        continue
    else:
        print(factores_contaminacion[0])
        continue