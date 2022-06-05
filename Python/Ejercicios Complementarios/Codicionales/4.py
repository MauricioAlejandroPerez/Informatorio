'''
Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m.
'''
num_1 = int(input("Ingrese un numero:\n"))
num_2 = int(input("Ingrese un numero:\n"))

if (num_2 % num_1) == 0:
    print("El primer numero es divisor del segundo.")
else: print("El primer numero no es divisor del segundo.")