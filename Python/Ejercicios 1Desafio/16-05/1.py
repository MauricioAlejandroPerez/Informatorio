'''
1- Escribir un programa que pregunte el nombre del usuario en la consola 
y después de que el usuario lo introduzca muestre por pantalla la cadena 
¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya 
introducido.
Luego pida dos valores, los sume y muestre el resultado por pantalla.

Solución:


'''
name = input("Introduzca su nomrbre: \n")

print(f"Hola {name}!")
print("Por favor, a continuacion introduzca dos valores.")

a = int(input("Introduzca el primer valor: \n"))
b = int(input("Introduzca el segundo valor: \n"))
suma = a + b

print(f"El resultado de la suma de estos valores es: {suma}")






