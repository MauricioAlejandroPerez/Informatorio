'''
A partir del siguiente diagrama de clases, implementá clases y métodos para mostrar atributos.
.  ______________
. | |Vehiculos| | 
. |   Color     |
. |   Ruedas    |
. --------------
.       /\ 
.       |
._______|__________ 
|     |Coche|     |
|Velocidad (Km/h),| 
|Cilindrada (cc)  |
------------------
'''

class Vehiculos:
    

    def __init__(self, color,ruedas = 4):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculos):


    def __init__(self, color, velocidad, cilindrada, ruedas):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

coche_1 = Coche('amarillo', 50, 55,4 )
coche_2 = Vehiculos("verde")

