'''
Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.
'''
num_1 = int(input("Ingrese un numero:\n"))
num_2 = int(input("Ingrese un numero:\n"))
num_3 = int(input("Ingrese un numero:\n"))

if num_1 > num_2 and num_3:
    if num_2 > num_3:
        print(f"{num_1}, {num_2}, {num_3}")
    else:
        print(f"{num_1}, {num_3}, {num_2}")
elif num_2 > num_3:
    if num_1 > num_3:
        print(f"{num_2}, {num_1}, {num_3}")
    else:
     print(f"{num_2}, {num_3}, {num_1}")
else:
    if num_1 > num_2:
        print(f"{num_3}, {num_1}, {num_2}")
    else:
        print(f"{num_3}, {num_2}, {num_1}")