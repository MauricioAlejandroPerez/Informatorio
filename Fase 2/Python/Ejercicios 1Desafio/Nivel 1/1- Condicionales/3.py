'''
Para el uso de fertilizantes es necesario medir cuánto abarca un determinado 
compuesto en el suelo el cual debe existir en una cantidad de al menos 10% 
por hectárea, y no debe existir vegetación del tipo MATORRAL. Escribir un 
programa que determine si es factible la utilización de fertilizantes.
'''
fertilizante =  float(input("Indique proporcionalmente la cantidad de fertilizante a usar por hectarea: \n"))
matorral = int(input("Existen algun tipo de matorrales en la superficie a fertiliar?: \
                    \n1. SI\
                    \n2. NO\n"))

if fertilizante >= 10 and  matorral == 2:
        print("Es factible la utilizacion de fertilizantes en el area.")
else:
    print("No sera posible la utilizacion de fertilizantes en este area.")