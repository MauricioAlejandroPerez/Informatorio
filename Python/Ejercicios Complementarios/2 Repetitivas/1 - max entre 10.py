'''
1) Determinar el número mayor de 10 números ingresados.
'''
# Variables:
max_num = 0
contador = 0

# Inicializacion del programa:
print("Ingrese 10 numeros:")

while contador < 10:
        contador += 1
        num_ingresado = int(input(f"{contador}* numeros:\n"))
        if num_ingresado > max_num:
            max_num = num_ingresado
        continue

# Resultado:
print(f"El numero maximo es:  {max_num}")