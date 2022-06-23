'''
a = input("Ingrese su nombre:\n")
b = input("Ingrese su apellido:\n")
full_name = a +" "+ b
print(f"Hola, {full_name.title()}!\n", type(a))
'''

'''
Frase_inv = input("Ingrese una frase: ")
inv = ""
for letra in Frase_inv:
    inv = letra + inv
print(inv)
'''
'''
def palindromo(param):
  
    inv = param[::-1]

    if inv == param:
        print("Es palindromo")
    else: 
        print("No es palindromo")

palindromo(input("Es palindromo?: ").lower())
'''

'''
producto = input("Ingrese nombre del Producto:")
precio = float(input("Ingrese el precio del Producto:$ "))
unidades = int(input("Ingrese canidad de unidades:"))
costetotal = round(float(precio*unidades),2)
print(f"Producto    -   Precio-unitario    -  Unidades    -  Costo-total\
    \n{producto}    -> ${precio}    ->{unidades}    ->${costetotal}")
'''
'''
numero_users = int(input("Ingrese la cantidad de usuarios a cargar:\n"))

while numero_users > users_cargados:
    users_cargados = 0
'''
'''
edad = 17

if edad <= 12:
    print("entrada 20")
else edad > 12:
    print("entrada 50")
'''
'''
for i in range(1,11):
    if i % 2:
        print(i)
'''
'''
print("DIVISOR DE NÚMEROS")
dividendo = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))

if dividendo % divisor:
    print(f"La división no es exacta. Cociente: {dividendo // divisor} "
               f"Resto: {dividendo % divisor}")
else:
    print(f"La división es exacta. Cociente: {dividendo // divisor}")
'''
hec = float(input("hec"))
matorral = input("mat")
comp = float(input("comp"))

porc = comp * 100 / hec

print(porc)
if porc >= 10:
    print("si")