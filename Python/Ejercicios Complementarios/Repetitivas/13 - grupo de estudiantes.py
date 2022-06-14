'''
Un grupo de 100 estudiantes presentan un exámen de Física. Diseñe un diagrama que lea por cada estudiante 
la calificación obtenida y calcule e imprima:

A.- La cantidad de estudiantes que obtuvieron una calificación menor a 50.

B.- La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70.

C.- La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80.

D. La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
'''
import random

estudiantes = 0
menor_50 = 0
entre_50_70 = 0
entre_70_80 = 0
mayor_80 = 0

while estudiantes < 100:
    estudiantes += 1
    nota = random.randint(0, 100)
    
    if nota <= 50:
        menor_50 += 1
    elif nota <= 70 and nota > 50:
        entre_50_70 += 1
    elif nota <= 80 and nota > 70:
        entre_70_80 += 1
    elif nota > 80:
        mayor_80 += 1

print(f"La cantidad de estudiantes que obtuvieron una calificación menor a 50 es: {menor_50}.\
    \nLa cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70 es: {entre_50_70}.\
    \nLa cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80 es: {entre_70_80}.\
    \nLa cantidad de estudiantes que obtuvieron una calificación de 80 o más es: {mayor_80}.")