'''

6) Imprimir, contar y sumar los múltiplos de 2 que hay entre una serie de números,
tal que el segundo sea mayor o igual que el primero.

'''
# Declaracion de Variables:
SerieDeNumeros = []
ContadorDePares = 0
SumaDePares = 0
NumerosPares = []

# Inicio del algoritmo: 
print("Ingrese una serie de numeros o 'fin' para finalizar.")

while True:
    entrada = input("Ingrese un valor:\n")
    
    if entrada == "fin":
        break
    
    SerieDeNumeros.append(int(entrada))
    
for numero in SerieDeNumeros:
    if (numero % 2) == 0:
        ContadorDePares += 1
        SumaDePares += numero
        NumerosPares.append(numero)

NumerosPares.sort()

# Resulta en pantalla:
print(f"Los numeros ingresados son: {SerieDeNumeros}.")
print(f"Los numeros pares de esta serie son {ContadorDePares}: \
        \n{NumerosPares} \
        \nLa sumatoria de ellos es igual a: {SumaDePares}.")