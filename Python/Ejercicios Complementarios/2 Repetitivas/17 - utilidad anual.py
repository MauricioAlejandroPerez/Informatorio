'''
Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades si este se le asigna como un 
porcentaje de su salario mensual que depende de su antigüedad en la empresa de acuerdo con la sig. tabla:

Tiempo										   Utilidad

Menos de 1 año								5% del salario

Más de 1 año y hasta 5 años		            7% del salario

Más de 5 años y hasta 10 años               10% del salario

Más de 10 años								20% del salario
'''
valor_error = "\nValor ingresado incorrecto.\nIntente nuevamente."

# ProgramaL:
while True:
    # Condicion de cierre/Nuevo ingreso:
    cc = input("\nDesea calcular la utilidad de otro trabajador? (S/N)").lower()
    
    if cc == "n":
        print("Adios!")
        break
    elif cc != "s":
        print(valor_error)
        continue

    # Calculo de utiliad:
    salario = float(input("\nIngrese el salario mensual percibido por el trabajador: "))
    antiguedad = int(input("Ingrese la antiguedad del trabajador: "))

    if antiguedad < 1 and antiguedad >= 0:
        utilidad = 5
    elif antiguedad >= 1 and antiguedad <= 5:
        utilidad = 7
    elif antiguedad > 5 and antiguedad <= 10:
        utilidad = 10
    elif antiguedad > 10:
        utilidad = 20
    else:
        print(valor_error)
        continue
    
    # Resultado por pantalla:
    print(f"El sueldo del trabajador es de ${salario} y tiene {antiguedad} anios de antiguedad.\
        \nLa utilidad percibida sera igual a ${salario * (utilidad / 100):.2f} ({utilidad}% de su salario mensual).)")