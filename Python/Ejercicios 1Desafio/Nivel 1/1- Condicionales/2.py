'''
La contaminación del agua es cualquier cambio químico, físico o biológico en la calidad 
del agua que tiene un efecto dañino en cualquier cosa viva que consuma ese agua. Cuando 
seres humanos beben el agua contaminada tienen a menudo problemas de salud.

La contaminación del agua se detecta en los laboratorios,  donde pequeñas muestras de 
agua se analizan para diversos tipos de contaminantes. Los organismos vivos tales como 
pescados se pueden también utilizar para la detección de la contaminación del agua. 
Los cambios en su comportamiento o crecimiento nos demuestran,  que el agua en la que 
viven está contaminada.

Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores 
un programa en Python que dado el tamaño de un pez indique si su organismo está 
contaminado. Para ello tendremos 4 opciones:

Tamaño Normal: Mensaje "Pez en buenas condiciones"
Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
Tamaño sobredimensionado: Mensaje "Pez contaminado"
'''
print("Para determinar el grado de contaminacion del pez capturado,\
 debera ingresar una de las siguientes opciones: \n")

FishSize = int(input("1. Si el pez tiene un tamaño NORMAL. \
                     \n2. Si el pez esta por DEBAJO del tamaño normal. \
                     \n3. Si el pez esta un POCO POR ENCIMA del tamaño normal. \
                     \n4. Si el pez tiene un tamaño SOBREDIMENSIONADO.\n"))

if FishSize == 1:
    print(f"Ud. selecciono la opcion {FishSize}, su pez esta en buenas condiciones.")

elif FishSize == 2:
    print(f"Ud. selecciono la opcion {FishSize}, su pez tiene problemas de nutricion.")

elif FishSize == 3:
    print(f"Ud. selecciono la opcion {FishSize}, su pez tiene síntomas de organismo contaminado.")

elif FishSize == 4:
    print(f"Ud. selecciono la opcion {FishSize}, su pez esta contaminado.")

else:
    print("La opcion seleccionada es erronea.")