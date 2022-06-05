'''
La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo 
al nombre de la barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)

La sección A esta formada por los barrios céntricos cuyo nombre comienza con una 
letra anterior a M y los barrios no céntricos con nombre posterior a la M, y la 
sección B el resto.

Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe 
en que sección se encuentra.
'''
barrio = input("Ingrese el nombre del barrio: \n").lower()
zona = int(input("Ingrese la zona del barrio: \
            \n1. Centrico.\
            \n2. No centrico.\n"))

# Seccion A = a-l y centrico o m-z no centrico
# Seccion B = a-l y no centrico o m-z centrico

if zona == 1:
    if barrio < "m":
        print("El barrio pertenece a la Seccion A")
    else:
        print("El barrio pertenece a la Seccion B")
else:
    if barrio < "m":
        print("El barrio pertenece a la Seccion B")
    else:
        print("El barrio pertenece a la Seccion A")
