'''
Si tiene 3 varillas, posiblemente de diferentes longitudes, puede o no ser posible colocarlas para que formen un 
triángulo cuando sus extremos se toquen. Por ejemplo, si todas las varillas tienen una longitud de 6 centímetros. 
entonces uno puede construir fácilmente un triángulo equilátero con ellos. Sin embargo, si una varillas es de 6 
centímetros de largo, mientras que los otros dos son cada uno de solo 2 centímetros de largo, entonces no se puede 
formar un triángulo. En general, si una longitud es mayor o igual que la suma de las otras dos, entonces las 
longitudes no pueden usarse para formar un triángulo. De lo contrario, pueden formar un triángulo. Escriba una 
función que determine si tres longitudes pueden formar un triángulo. La función tomará 3 parámetros y devolverá un 
resultado booleano. Además, escriba un programa que lea 3 longitudes del usuario y muestre el comportamiento de esta 
función.
'''
triangulo = lambda l1, l2, l3: not(l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2))

while True:
    print("Ingrese a contunuacion uno a uno la longitud de los lados para determinar si se trata de un triangulo.")
    l1 = int(input("Ingrese la longitud de uno de los lados: "))
    l2 = int(input("Ingrese la longitud de otro de los lados: "))
    l3 = int(input("Ingrese la longitud del lado restante: "))

    print(triangulo(l1, l2, l3))