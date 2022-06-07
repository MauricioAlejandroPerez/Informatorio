'''
Realizar un programa que calcule y muestre la suma de los múltiplos de 5 comprendidos entre dos 
valores A y B. El programa no permitirá introducir valores negativos para A y B y verificará que 
A es menor que B. Si A es mayor que B, se deben intercambiar los valores.
'''
while True:
    # Declarcion de variables:
    print("Ingrese dos valores enteros positivos.")
    valor_uno = int(input("Ingrese el primer valor:\n"))
    valor_dos = int(input("Ingrese un segundo valor:\n"))
    suma_multiplos = 0

    # Algoritmo:
    if valor_uno < 0 or valor_dos < 0:
        print("Los valores ingresados no cumplen con los requisitos solicitados.\
            \nIntente nuevamente.") 
        continue
    elif valor_uno > 0 and valor_dos > 0:
        if valor_uno > valor_dos: # Con esto consigo invertir las variables, de ser necesario.
            valor_uno, valor_dos = valor_dos, valor_uno
        for num in range(valor_uno, valor_dos + 1):
                if (num % 5) == 0:
                    suma_multiplos += num
    # Resultado:                    
    print(f"La suma de los multiplos de 5 entre los valores {valor_uno} y {valor_dos} es igual a: {suma_multiplos}")
    if input("Desea volver a intentarlo? (S/N)\n").lower() == "s":
        continue
    else: break
    