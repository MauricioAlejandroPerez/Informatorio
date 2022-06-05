'''
2) Desarrollar una solución que calcule la suma de los cuadrados de los n primeros números naturales: 1 + 22 + 32 +… + n2.
'''
# Iniciacion de variable:
sumatoria = 0

#Programa:
for num in range(1, 10):
    sumatoria += num ** 2

# Resultado:
print(sumatoria)

# Comprobacion:
# comp = 0**2+1 + 2**2+ 3**2+4**2+5**2+6**2+7**2+8**2+9**2
# print(comp)