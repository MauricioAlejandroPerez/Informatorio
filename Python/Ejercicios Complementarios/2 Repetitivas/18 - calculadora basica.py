'''
Diseña un programa al que se proporcione como entradas dos enteros y un carácter. 
El programa deberá sumar, restar, multiplicar o dividir los valores de los dos primeros parámetros 
dependiendo del código indicado en el tercer parámetro, y devolver el resultado. Por ejemplo si el 
usuario ingresa la opción “S”, se deberán sumar los números.
'''
valor_error = "\nValor ingresado incorrecto.\nIntente nuevamente."

print("Inicializando calculadora basica.")
while True:
    # Condicion de cierre/Nuevo ingreso:
    cc = input("\nDesea realizar una operacion matematica? (S/N)").lower()
    
    if cc == "n":
        print("Adios!")
        break
    elif cc != "s":
        print(valor_error)
        continue

    print("A continuacion ingrese dos numeros enteros.")
    num_1 = int(input("Ingrese el primer numero: "))
    num_2 = int(input("Ingrese el segundo numero: "))

    operacion = input("Ingrese la operacion que desea realizar:\
                    \nS. Suma.\
                    \nR. Resta\
                    \nM. Multiplicacion.\
                    \nD. Division.\
                    \nQ. Salir.").lower()
    
    if operacion == "s":
        res = num_1 + num_2
    elif operacion == "r":
        res = num_1 - num_2
    elif operacion == "m":
        res = num_1 * num_2
    elif operacion == "d":
        res = num_1 / num_2
    else:
        print(valor_error)
        continue

    # Resultado en pantalla:
    print(f"El resultado de la operacion matematica es: {res}")