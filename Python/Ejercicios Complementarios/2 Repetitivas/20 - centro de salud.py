'''
El Centro de Salud de Rosario tiene registradas N consultas médicas de menores. De cada consulta tiene 
como datos: la edad del menor y el día de visita. Los datos están ordenados en forma creciente por día. 
Proponer un fin de datos para cada día. Se desea conocer, para cada día, la edad promedio de pacientes 
y además el día en que se registró el máximo de pacientes.
'''
# Declaracion de variables:
mayor_promedio = 0
fecha_mayor_promedio = ""
dia_carga = 0
mes_carga = 0
anio_carga = 0
valor_error = "\nValor ingresado incorrecto.\nIntente nuevamente."

# Algoritmo:
print("Software de Estadisticas del Centro de Salud de Rosario.")
while True:
    # Otras variables necesarias dentro del bucle:
    promedio_diario = 0
    menores_atendidos = 0
    fecha_carga = ""

    # Ingreso / Condicion de cierre:
    cc = input("\nDesea cargar datos? (S/N)").lower()
    
    if cc == "n":
        print("\nCerrando el software de Estaditicas del Centro de Salud de Rosario")
        break
    elif cc != "s":
        print(valor_error)
        continue
    
    # Determinacion de la fecha:
    print("\nA continuacion ingrese la fecha que desea cargar:")
    anio_carga = int(input("Ingrese el anio: "))
    if anio_carga < 2004  or anio_carga > 2022:
        print(valor_error)
        continue

    mes_carga = int(input("Ingrese el mes: "))
    if mes_carga < 0 or mes_carga > 12:
        print(valor_error)
        continue
    
    dia_carga = int(input("Ingrese el dia: "))
    if mes_carga == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        if dia_carga < 0 or dia_carga > 31:
            print(valor_error)
            continue
    elif mes_carga == (4 or 6 or 9 or 11):
        if dia_carga < 0 or dia_carga > 30:
            print(valor_error)
            continue
    elif mes_carga == 2:
        if dia_carga < 0 or dia_carga > 29:
            print(valor_error)
            continue

    fecha_carga = str(dia_carga) + "/" + str(mes_carga) + "/" + str(anio_carga)

    # Datos de la edad:
    while True:
        print(f"\n{menores_atendidos} menores atendidos el dia de hoy.")
        edad = int(input("Ingrese la edad del menor atendido (0 para salir): "))
        
        if edad == 0:
            print("Fin de los datos cargados para este dia.")

            promedio_diario = promedio_diario / menores_atendidos
            print(f"\nEl dia {fecha_carga} se atendiareon {menores_atendidos} menores de edad.\
                \nCon un promedio de edad de {promedio_diario:.2f} anios.")
            
            break
        elif edad > 0 and edad < 18:
            promedio_diario += edad
            menores_atendidos += 1
        else:
            print(valor_error)
            continue
    
    # Registro del mayor promedio:
    if promedio_diario > mayor_promedio:
        mayor_promedio = promedio_diario
        fecha_mayor_promedio = fecha_carga

    print(f"\nEl mayor promedio de edad registrado fue: {mayor_promedio:.2f} anios.\
        \nLa fecha en que se registro fue el dia {fecha_mayor_promedio}.")

print(f"\nEl mayor promedio de edad registrado fue: {mayor_promedio:.2f} anios.\
        \nLa fecha en que se registro fue el dia {fecha_mayor_promedio}.")