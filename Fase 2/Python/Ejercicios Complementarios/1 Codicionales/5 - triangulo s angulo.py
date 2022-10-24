'''
Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) y determine qué tipo
de triángulo es, de acuerdo a los siguientes casos. Suponiendo que A determina el mayor de los tres lados y
B y C corresponden con los otros dos, entonces:

Si A>=B + C à No se trata de un triángulo

Si A2 = B2 + C2 à Es un triángulo rectángulo

Si A2 > B2 + C2 à Es un triángulo obtusángulo

Si A2 < B2 + C2 à Es un triángulo acutángulo
'''
l1 = int(input("Ingrese la longitud del mayor de los lados:\n"))
l2 = int(input("Ingrese la longitud de otro de los lados:\n"))
l3 = int(input("Ingrese la longitud del lado restante:\n"))

print(l1 >= (l2 + l3))
if l1 >= (l2 + l3):
    print("No se trata de un triangulo.")
elif (l1 ** 2) == (l2 ** 2 + l3 ** 2):
    print("Se trata de un triangulo RECTANGULO.")
elif (l1 ** 2) >= (l2 ** 2 + l3 ** 2):
    print("Se trata de un triangulo OBTUSANGULO.")
elif (l1 ** 2) <= (l2 ** 2 + l3 ** 2):
    print("Se trata de un triangulo ACUTANGULO.")