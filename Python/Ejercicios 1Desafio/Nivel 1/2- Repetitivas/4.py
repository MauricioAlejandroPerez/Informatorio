'''
Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de acuerdo 
al tamaño indicado. Por ejemplo el gráfico a la izquierda es el resultado de un tamaño: 8x6
'''
'''
   --------------------------
  |      CON LISTAS         |
  --------------------------

# Variables:
green = "|V|"
white = "|B|"
count = 0
casilla_h1 = [] # |V||B|
casilla_h2 = [] # |B||V|

# Variables definidas por el usuario
print("Ingrese las dimensiones del tablero ecologico que desea crear.")
tab_ancho = int(input("Cuantas casillas horizontales desea que tenga:\n"))
tab_alto = int(input("Cuantas casillas verticales desea que tenga:\n"))

# Algoritmo:
# Generador de casillas:
for num in range(tab_ancho):
    if  (num % 2 == 0):
        casilla_h1.append(green)
    else: casilla_h1.append(white)
    
for num in range(tab_ancho):
    if  (num % 2 == 0):
        casilla_h2.append(white)
    else: casilla_h2.append(green)

# Resultado - Armado de tablero:
while count < tab_alto:
    count += 1
    if (count % 2 == 0):
        for i, casilla in enumerate(casilla_h1):
            if i != len(casilla_h1)-1:
                print(casilla, end=""),
            else: print(casilla)
    else:
        for i, casilla in enumerate(casilla_h2):
            if i != len(casilla_h2)-1:
                print(casilla, end=""),
            else: print(casilla)
'''
#  --------------------------
# |      CON STRINGS        |
# --------------------------

# Variables:
verde = "|V|"
blanco = "|B|"
count = 0
casilla_h1 = "" # |V||B|
casilla_h2 = "" # |B||V|

# Variables definidas por el usuario
print("Ingrese las dimensiones del tablero ecologico que desea crear.")
tab_ancho = int(input("Cuantas casillas horizontales desea que tenga:\n"))
tab_alto = int(input("Cuantas casillas verticales desea que tenga:\n"))

# Algoritmo:
# Generador de casillas:
for num in range(tab_ancho):
    if  (num % 2 == 0):
        casilla_h1 = casilla_h1 + verde
    else: casilla_h1 = casilla_h1 + blanco
    
for num in range(tab_ancho):
    if  (num % 2 == 0):
        casilla_h2 = casilla_h2 + blanco
    else: casilla_h2 = casilla_h2 + verde

# Resultado - Armado de tablero:
while count < tab_alto:
    count += 1
    if (count % 2 == 0):
        print(casilla_h1)
    else:
        print(casilla_h2)