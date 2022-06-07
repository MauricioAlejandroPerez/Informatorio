'''
Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio de tres 
calificaciones es mayor o igual a 70; desaprueba en caso contrario.
'''
calificacion_1 = float(input("Ingrese la primera calificacion:\n"))
calificacion_2 = float(input("Ingrese la segunda calificacion:\n"))
calificacion_3 = float(input("Ingrese la tercera calificacion:\n"))
calificacion_promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3

if calificacion_promedio >= 7:
    print(f"El alumno APROBO el curso con una nota promedio de {calificacion_promedio:.2f}.")
elif calificacion_promedio <= 7:
     print(f"El alumno DESAPROBO el curso con una nota promedio de {calificacion_promedio:.2f}.")
else:
    print("El valor ingresado es incorrecto.")