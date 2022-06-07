'''
Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:

i. Si trabaja 40 horas o menos se le paga $16 por hora

ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.
'''
horas_trabajadas = int(input("Cuantas horas ha trabajado la semana que desea calcular:\n"))

if horas_trabajadas <= 40:
    salario_semanal = horas_trabajadas * 16
elif horas_trabajadas > 40:
    salario_semanal = 40 * 16 + (horas_trabajadas - 40) * 20

print(f"El salario de esta semana es de ${salario_semanal}.")