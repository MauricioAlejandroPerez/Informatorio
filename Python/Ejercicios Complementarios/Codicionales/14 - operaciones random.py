'''
Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los 
reste y si no que los sume.
'''
import random

num_1 = random.randint(1, 10)
num_2 = random.randint(1, 10)

if num_1 == num_2:
    res = num_1 * num_2
    print(f"El producto de {num_1} y {num_2} es igual a {res}.")
elif num_1 > num_2:
    res = num_1 - num_2
    print(f"La diferencia entre {num_1} y {num_2} es igual a {res}.")
else:
    res = num_1 + num_2
    print(f"La adicion de {num_1} y {num_2} es igual a {res}.")