'''
Se tiene una lista con los datos de los clientes de una compañía de telefonía celular, los cuales pueden 
aparecer repetidos en la lista, si tienen registrado más de un número telefónico. La compañía para su 
próximo aniversario desea enviar un regalo a sus clientes, sin repetir regalos a un mismo cliente. En una 
lista se almacenan los regalos disponibles en orden. Se desea un programa que cree una nueva lista con los 
clientes, sin repetir y ordenada. Y que al final muestre el regalo que le corresponde a cada cliente.
'''
numeros_telefonicos = [
    {"Nombre" : "Paez, Ariel",
    "Telefono" : 123,
    "Id. Cliente" : 1},

    {"Nombre" : "Alvarez, Angel",
    "Telefono" : 345,
    "Id. Cliente" : 2},

    {"Nombre" : "Paez, Ariel",
    "Telefono" : 213,
    "Id. Cliente" : 1},

    {"Nombre" : "Paez, Ariel",
    "Telefono" : 321,
    "Id. Cliente" : 4},

    {"Nombre" : "Bogarin, Natalia",
    "Telefono" : 567,
    "Id. Cliente" : 3}
]

regalos_disponibles = ["Manzana", "Naranja", "Mandarina", "Pera"]

# Individualizacion de clientes:
lista_clientes = []

# Armando lista de diccionarios donde contega una sola vez a cada cliente con su Id.
for dic in numeros_telefonicos:
    if ({dic["Id. Cliente"]: dic["Nombre"]}) not in lista_clientes:
        lista_clientes.append({dic["Id. Cliente"]: dic["Nombre"]})

# Ahora esos diccionarios los agrupamos con el cliente en un str para poder ordenarlos.
lista_clientes[:] = [f"{ID}: {nombre}" for dic in lista_clientes for ID, nombre in dic.items()]
lista_clientes.sort()

# Por cada cliente otorgamos un regalo:
lista_cliente_regalo = {}

for cliente in lista_clientes:
    lista_cliente_regalo[cliente] = regalos_disponibles.pop()
    print(f"El cliente '{cliente}' recibira {lista_cliente_regalo[cliente]} como regalo de la compania.")

