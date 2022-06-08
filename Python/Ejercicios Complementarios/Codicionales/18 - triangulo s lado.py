'''
Se leen tres números que son las longitudes de los lados de un triángulo. Determinar e informar 
si el mismo es equilátero (3 lados iguales), isósceles (2 lados iguales) o escaleno (3 lados distintos).
'''
l1 = int(input("Ingrese la longitud de uno de los lados:\n"))
l2 = int(input("Ingrese la longitud de otro de los lados:\n"))
l3 = int(input("Ingrese la longitud del lado restante:\n"))

if l1 >= (l2 + l3) or l2 >= (l1 + l3) or l3 >= (l1 + l2):
    print("No se trata de un triangulo.")
elif l1 == l2 and l1 == l3:
    print("Es un triangulo EQUILATERO.")
elif l1 == l2 or l1 == l3:
    print("Es un triangulo ISOCELES.")
elif l1 != l2 and l1 != l3:
    print("Es un triangulo ESCALENO.")