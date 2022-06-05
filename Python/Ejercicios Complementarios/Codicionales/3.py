'''
Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos.
'''
num_1 = int(input("Ingrese un numero:\n"))
num_2 = int(input("Ingrese un numero:\n"))
num_3 = int(input("Ingrese un numero:\n"))

if num_1 < num_2 and num_3:
    print("Si, el primer numero es menor a los demas.")
else: print("No, el primer numero no es menor a los demas.")
    
