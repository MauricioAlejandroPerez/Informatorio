'''
Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados 
para el ambiente.

a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa 
debe preguntar al usuario la contraseña, y no le permita continuar hasta que la haya 
ingresado correctamente.

b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos. 
'''
password = "asd"

# a)
# while input("Ingrese contraseña correcta para continuar: \n") != password:
    # print("Contraseña incorrecta, intenten nuevamente.")
    # continue
# else:
    # print("Contraseña correcta, has conseguido ingresar.")


# b)
# Contador de intentos fallidos:
intentos = 3

# Algoritmo para ingreso de clave:
while intentos > 0:
    passIngresado = input("Ingrese contraseña correcta para continuar: \n")
    if  passIngresado != password:
        intentos -= 1
        print(f"Contraseña incorrecta. Tiene {intentos} intentos restantes.")
        continue
    else:
        print("Contraseña correcta, has conseguido ingresar.")
        break
else:
   print("Ud. ha agotado todos los intentos disponibles.")
        