'''
Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar). 
Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos.
'''
# Variables iniciales
agenda = {
    "emergencias": 911
}

# Algoritmo
print("Agenda de correos de biologos.")
while True:

    cc = int(input("\nSeleccione una opcion:"
            "\n1. Consultar agenda."
            "\n2. Agregar contacto."
            "\n3. Borrar contacto."
            "\n0. Salir\n"))

    if cc == 0: # Condicion de Salida
        print("Adios!")
        break
    elif cc == 1: # Consultar la agenda
        for contacto in agenda:
            print(f"{contacto}: {agenda[contacto]}")
            continue
    elif cc == 2: # Agregar un contacto
        nombre = input("Ingrese el nombre del biologo: ")
        email = input("Ingrese correo electronico del biologo: ")

        if nombre not in agenda:
            agenda[nombre] = email
            print(f"\nSe ha agendado correctamente a {nombre}")
            continue
        else:
            print("\nEse contacto ya se encuentra agendado.")
            continue
    elif cc == 3: # Borrar un contacto
        nombre = input("Ingrese el nombre del contacto que desea eliminar: ")

        if nombre in agenda:
            del(agenda[nombre])
            print(f"El contacto {nombre} ha sido eliminado correctamente.")
            continue
        elif nombre not in agenda:
            print(f"El contacto {nombre} no existe.")
            continue
    else: # Opcion incorrecta
        print("La opcion ingresada es incorrecta, intente nuevamente.")
        continue