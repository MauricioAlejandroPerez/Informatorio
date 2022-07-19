'''
Las palabras como primero, segundo y tercero se refieren a números ordinales. En este ejercicio, escribirá 
una función que toma un número entero como su único parámetro y devuelve una cadena que contiene el número 
ordinal apropiado como único resultado. Su función debe manejar los enteros entre 1 y 12 (inclusive). 
Debería devolver una cadena vacía si se proporciona un valor fuera de este rango como parámetro. Incluya un 
programa principal que utilice su función mostrando cada número entero del 1 al 12 y su número ordinal.
'''
def ordinal(numero):    
    if numero == 1:
        num_ord = "primero"
    elif numero == 2:
        num_ord = "segundo"
    elif numero == 3:
        num_ord = "tercero"
    elif numero == 4:
        num_ord = "cuarto"
    elif numero == 5:
        num_ord = "quinto"
    elif numero == 6:
        num_ord = "sexto"
    elif numero == 7:
        num_ord = "septimo"
    elif numero == 8:
        num_ord = "octavo"
    elif numero == 9:
        num_ord = "noveno"
    elif numero == 10:
        num_ord = "decimo"
    elif numero == 11:
        num_ord = "onceavo"
    elif numero == 12:
        num_ord = "doceavo"
    else:
        num_ord = ""
    
    print(num_ord)

while True:
    ingreso = int(input("Ingrese un numero ordinal del 1 al 12: "))

    ordinal(ingreso)