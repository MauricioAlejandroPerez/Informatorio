'''
Escriba una función que tome las longitudes de los dos lados más cortos de un triángulo rectángulo como 
sus parámetros y devuelva la hipotenusa del triángulo, calculada usando el teorema de Pitágoras, como 
resultado de la función. Incluya un programa principal que lea las longitudes de los lados más cortos de 
un triángulo rectángulo del usuario, use su función para calcular la longitud de la hipotenusa y muestre 
el resultado.
'''
Hipotenusa = lambda l1, l2 : (l1 ** 2 + l2 ** 2) ** (.5)

lado1 = float(input("Cuanto mide el primer lado? "))
lado2 = float(input("Cuanto mide el segundo lado? "))

print(f"La hipotenusa del triangulo es igual a {Hipotenusa(lado1, lado2)}")