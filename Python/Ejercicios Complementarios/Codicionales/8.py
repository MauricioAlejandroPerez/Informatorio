'''
Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, 
si la fórmula es: Número de pulsaciones = (220 - edad)/10
'''
edad = int(input("Ingrese su edad:\n"))
pulsaciones = (220 - edad) / 10

print(f"El numero de pulsaciones de una persona es de {pulsaciones:.2f} cadca 10 segundos.")