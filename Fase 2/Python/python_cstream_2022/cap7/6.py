suma = 0
while True:

    valor = input("Ingrese un número. Para terminar ingrese la palabra quit: ")

    if valor.upper() == 'QUIT':
        break

    try:
        suma += int(valor)
    except ValueError:
        print("invalid value!")
        break

print(f"el resultado es {suma}")