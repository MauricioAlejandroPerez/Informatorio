'''
Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores 
con un aumento del salario para la siguiente campaña. Los sueldos deben ajustarse 
de la siguiente forma:

Sueldo Actual (en $)      Aumento

0 – 6000					15%

6000 – 7900				   10%

7900 – 12000				6%

Más de 12000			   0%

Diseñar un programa que lea el salario de un jugador, y que a continuación muestre 
el tanto por ciento de aumento, el sueldo actual y el sueldo aumentado.
'''

SueldoActual = int(input("Ingrese el sueldo percibido por el jugador: \n"))

if 0 < SueldoActual <= 6000:

    SueldoActualizado = SueldoActual * 1.15
    print(f"El jugador recibira un aumento del su sueldo del 15% respecto de mismo. \
    \nPor lo tanto pasara de percibir ${SueldoActual:.02f}, a percibir ${SueldoActualizado:.02f}.")
    
elif 6000 < SueldoActual <= 7900:
    
    SueldoActualizado = SueldoActual * 1.1
    print(f"El jugador recibira un aumento del su sueldo del 10% respecto de mismo. \
    \nPor lo tanto pasara de percibir ${SueldoActual:.02f}, a percibir ${SueldoActualizado:.02f}.")    

elif 7900 < SueldoActual <= 12000:
    
    SueldoActualizado = SueldoActual * 1.06
    print(f"El jugador recibira un aumento del su sueldo del 6% respecto de mismo. \
    \nPor lo tanto pasara de percibir ${SueldoActual:.02f}, a percibir ${SueldoActualizado:.02f}.")
    
elif 12000 < SueldoActual:
    
    SueldoActualizado = SueldoActual * 1
    print(f"El jugador no recibira aumento salarial. \
    \nPor lo tanto percibira ${SueldoActual:.02f}.")
    
else: 
    print("Debe ingresar un valor superior a 0.")

