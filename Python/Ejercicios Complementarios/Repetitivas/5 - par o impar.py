'''
Solicitar el ingreso de números al usuario y emitir un mensaje para determinar si es par o impar. 
El ciclo debe finalizar cuando el usuario ingresa 0.
'''
while True:
    numero = int(input("Ingrese un numero:\n"))
    if numero == 0:
        print("Fin del programa.")
        break
    elif (numero % 2) == 0:
        print("Es par.")
    else:
        print("Es impar.")