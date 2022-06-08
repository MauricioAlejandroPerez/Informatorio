'''
Mostrar los perímetros de varios triángulos ingresados sus lados por teclado, hasta que ya no desee.
'''
while True:
    print("Ingrese a contunuacion uno a uno los lados del triangulo para calcular su perimetro.")
    l1 = int(input("Ingrese la longitud de uno de los lados:\n"))
    l2 = int(input("Ingrese la longitud de otro de los lados:\n"))
    l3 = int(input("Ingrese la longitud del lado restante:\n"))

    if l1 >= (l2 + l3) or l2 >= (l1 + l3) or l3 >= (l1 + l2):
        print("No se trata de un triangulo.")
        continue
    else:
        print(f"El perimetro del triangulo es igual a {(l1 + l2 + l3)}.")
    
    cc = input("Desea calcular otro perimetro? (S/N): ").lower
    if cc == "s":
        continue
    else:
        break