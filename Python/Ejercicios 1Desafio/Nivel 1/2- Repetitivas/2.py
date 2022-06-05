'''
Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.

Realizá un programa que permita registrar cantidad de colillas recolectadas por un número determinado de personas. 
Luego obtener estadísticas al respecto informando porcentaje de personas que han encontrado menos de 100 colillas, 
más de 100 y menos de 200, más de 200 colillas.
'''
# Iniciacion de variables requeridas:
Recolectores = 0
menos100 = 0
entre100y200 = 0
mas200 = 0

# Contador de recolectores:
print("Ingrese la cantidad de colillas recolectada por cada persona o 'fin' para finalizar.")
while True:
    entrada = input("Cuantas colillas junto?:\n")
    
    if entrada == "fin":
        break
    
    entrada = int(entrada)
    if entrada <= 100:
        menos100 += 1
    elif  entrada > 100 and entrada <= 200:
        entre100y200 += 1
    elif entrada > 200:
        mas200 += 1
    
    Recolectores += 1

# Resultado en pantalla:
print("\nLas estadisticas de los recolectores son las siguientes:")
print(f"El {(menos100/Recolectores*100):.2f}% recolectaron 100 colillas o menos.")
print(f"El {(entre100y200/Recolectores*100):.2f}% recolectaron entre 100 y 200 colillas.")
print(f"El {(mas200/Recolectores*100):.2f}% recolectaron mas de 200 colillas.")