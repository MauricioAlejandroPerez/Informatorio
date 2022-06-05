'''
Repetitivas - Ejercicio 16
Escribir un programa el cual lea dos valores enteros. 
Si el primero es menor que el segundo, que imprima el mensaje Arriba''. 
Si el segundo es menor que el primero, que imprima el mensaje Abajo''. 
Si los números son iguales, que imprima el mensaje igual''. 
Si alguno de los datos ingresados es igual a 0, 
que imprima un mensaje conteniendo la palabra Error''.


#Version 1:
valor_uno = int(input("Ingrese un valor entero:\n"))
valor_dos = int(input("Ingrese un segundo valor entero:\n"))

#while valor_uno!=0 and valor_dos!=0:
while valor_uno>0 and valor_dos>0:
    if valor_uno < valor_dos:
        print('ARRIBA')
    elif valor_dos <  valor_uno:
        print('ABAJO')
    else:
        print('IGUALES')
    valor_uno = int(input("Ingrese un valor entero:\n"))
    valor_dos = int(input("Ingrese un segundo valor entero:\n"))
else:
    print('Error. Ha ingresado un valor incorrecto')


Versión 2:
'''
while True:
    valor_uno = int(input("Ingrese un valor entero:\n"))
    valor_dos = int(input("Ingrese un segundo valor entero:\n"))
    if valor_uno>0 and valor_dos>0:
        if valor_uno < valor_dos:
            print('ARRIBA')
        elif valor_dos <  valor_uno:
            print('ABAJO')
        else:
            print('IGUALES')
    else:
        print('Error. Ha ingresado un valor incorrecto')
        break
