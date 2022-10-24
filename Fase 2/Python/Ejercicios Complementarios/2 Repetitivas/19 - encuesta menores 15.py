'''
Dados los datos de un municipio: zona, sexo y edad de cada uno de sus habitantes, encontrar:

a) porcentaje de varones menores de 15 años para cada zona

b) porcentaje de varones menores de 15 años para todo el municipio

Los datos vienen ordenados por zona.Con dato de zona igual a 0, se indica el fin.
'''
from re import T


valor_error = "\nValor ingresado incorrecto.\nIntente nuevamente."
zona_centro = 0
zona_periferica = 0

print("Programa de censo adolenscente del municipio.")

while True:
    # Condicion de cierre/Nuevo ingreso:
    cc = int(input("\nZona de residencia del adolescente encuestado:\
        \n1. Zona CENTRO.\
        \n2. Periferia.\
        \n0. Salir del programa."))
    
    if cc == 0:
        break
    elif cc != 1 and cc != 2:
        print(valor_error)
        continue
    
    edad = int(input("Edad del adolescente encuestasdo: "))

    if edad < 15:
        if cc == 1:
            zona_centro += 1
        elif cc == 2:
            zona_periferica += 1
    
    print("No hay mas preguntas, muchas gracias.")

total = zona_centro + zona_periferica
# Resultado por pantalla:
print(f"\nDel total de varones entrevistados, menores a 15 anios:\
        \nEl {((zona_centro / total) * 100):.2f}% pertenece a la ZONA CENTRO del municipiol.\
        \nEl {((zona_periferica / total) * 100):.2f}% pertenece a la ZONA PERIFEFRICA del municipiol.\n")