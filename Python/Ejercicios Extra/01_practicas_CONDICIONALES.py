#print ("Hola Mundo")

"""
la sangría en Python es muy importante.

Python usa sangría para indicar un bloque de código
Establecer una sangría se denomina IDENTAR O IDENTACIÓN.

(PARA INSERTAR COMENTARIOS, USAMOS:
numeral...Para 1 sola linea;
triple comillas... Para englobar un texto, poniendo al principio y al final del texto)
"""
"""
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
"""

"""
Normalmente, cuando crea una variable dentro de una función, esa variable es LOCAL y solo se puede usar dentro de esa función.

Para crear una variable global dentro de una función, puede usar la "global" palabra clave.
"""
### FORMAS DE PONER LOS DIAS DE LA SEMANA:
                                        # PRIMERA FORMA, utilizando if y else:
"""
dia_semana = int(input("Ingrese un numero: "))
dia = None

if dia_semana == 1:
    dia = "Lunes"
else:
    if dia_semana ==2:
        dia = "Martes"
    else:
        if dia_semana == 3:
            dia = "Miercoles"
        else:
            if dia_semana == 4:
                dia = "Jueves"
            else:
                if dia_semana == 5:
                    dia = "Viernes"
                else:
                    if dia_semana == 6:
                        dia = "Sabado" 
                    else:
                        if dia_semana == 7:
                            dia = "Domingo"

if dia is None:
  print ("El numero asignado esta fuera del rango del 1 al 7.")
else:
  print("El dia de la semana es: ", dia) 
  """

                                        # SEGUNDA FORMA, utilizando elif:
"""                                       
dia_semana = int(input("Ingrese un numero: "))
dia = None

if dia_semana == 1:
    dia = "Lunes"
elif dia_semana ==2:
      dia = "Martes"
elif dia_semana == 3:
      dia = "Miercoles"
elif dia_semana == 4:
      dia = "Jueves"
elif dia_semana == 5:
      dia = "Viernes"
elif dia_semana == 6:
      dia = "Sabado" 
elif dia_semana == 7:
      dia = "Domingo"
else:
    print ("No ingreso ningun numero valido")

if dia is None:
  print ("El numero asignado esta fuera del rango del 1 al 7.")
else:
  print("El dia de la semana es: ", dia)
"""



                                        # TERCERA FORMA, comparando listas:
"""
DIAS_DE_LA_SEMANA = [" ", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
numero_de_dia = [1, 2, 3, 4, 5, 6, 7]



"""
"""
EJERCICIO 1:
Un local vende ropa al por menor y mayor. Si la compra es por una cantidad igual a 10 remeras, el precio por unidad es de tan solo del 80%.
Preguntar cuantas unidades de remeras se incluyen en la compra y el precio por unidad.
Devolver el precio total de la compra.

"""
"""
print("Buen día")
Q = int(input("Ingrese la cantidad vendida: "))
P = float(input("Ingrese el precio: "))

if Q>= 10:
    print("El monto a cobras es: ", Q*(P*0.8))
else:
    print("El monto a cobras es: ", Q*P)

print("Muchas gracias")
"""
"""
EJERCICIO 2:
Ingresar la edad de una persona, indicando/mostrando si es menor de edad o mayor.
"""
"""
print("Hola, mucho gusto.")
edad = int(input("Ingresar su edad: "))
if edad < 18:
    print("Es menor de edad.")
else:
    print("Es mayor de edad.")
"""
"""
EJERCICIO DE CLASE:
Se debe hacer un programa que nos calcule cuanto dinero se desembolsaria en una compra. Sabiendo que si el importe sumado es superior a $1500 se aplica el 30% de descuento.
Si es superior a $1000 se aplica el 20%. Y si es superior a $750 solo el 10%.

"""
"""
Monto = float(input("Ingrese el monto total sujeto a descuento: "))
if Monto >= 1500:
    print("El descuento aplicado es del 30%")
    Monto_a_Cobrar=Monto * (1-0.3)
    print("El total a cobrar es: $", Monto_a_Cobrar)
elif Monto>=1000:
    print("El descuento aplicado es del 20%")
    Monto_a_Cobrar=Monto * (1-0.2)
    print("El total a cobrar es: $", Monto_a_Cobrar)
elif Monto>=750:
    print("El descuento aplicado es del 10%")
    Monto_a_Cobrar=Monto * (1-0.1)
    print("El total a cobrar es: $", Monto_a_Cobrar)
else:
    print("No se aplica descuento.")
    Monto_a_Cobrar=Monto * 1
    print("El total a cobrar es: $", Monto_a_Cobrar)

"""

### DESAFIOS EJERCICIOS CONDICIONALES
""" DESAFIO 1:
Se necesita calcular el resultado final de un cuestionario realizado por una persona.
Solicita cantidad total de preguntas y luego cantidad de respuestas correctas.
Si el porcentaje de respuestas correctas es mayor o igual a 90, el resultado es EXCELENTE. 
Si el porcentaje de respuestas correctas es mayor o igual a 70, el resultado es BUENO. 
Si el porcentaje de respuestas correctas es mayor o igual a 60, el resultado es APROBADO. 
Si el porcentaje de respuestas correctas es menor a 60, el resultado es NO ALCANZÓ.  
"""
"""
q_preguntas = int(input("Ingrese la cantidad de preguntas realizadas: "))
q_respuestas = int(input("Ingrese la cantidad de respuestas correctas: "))

resultado = (q_respuestas/q_preguntas)*100

if resultado >= 90:
    print("El resultado final obtenido es EXCELENTE, su puntaje es: ", resultado)
elif resultado >=70:
    print("El resultado final obtenido es BUENO, su puntaje es: ", resultado)
elif resultado >= 60:
    print("El resultado final obtenido es APROBADO, su puntaje es: ", resultado)
else:
    print("El resultado final obtenido NO ALCANZO, su puntaje es: ", resultado)

"""
"""
Actividad DE LA CLASE:
Los alumnos de un curso se han dividido en 2 grupos, A y B. De acuerdo al nombre y al sexo.
El grupo A, esta formado por las mujeres con un nombre anterior a la M y hombres con un nombre posterior a la N.
El grupo B, por el resto. Escribir un programa que pregunte al usuario el nombre y el sexo, y muestre por pantalla el grupo que le corresponde.
"""
"""
print("Hola. Mucho gusto, vamos a asignarle el grupo al que pertenece.")

nombre_alumnos= input("Ingrese su nombre: ")
nombre_alumnos_lower = nombre_alumnos.lower()

sexo_alumnos= input("Ingrese su sexo (F/M): ")
#ACA PODRIAMOS AGREGAR UN WHILE PARA QUE EN EL CASO DE QUE LA PERSONA INGRESE VALORES DISTINTOS A "F" ó "M", ME REPITA EL BUCLE HASTA QUE INGRESE CORRECTAMENTE.

sexo_alumnos_upper = sexo_alumnos.upper()
print(sexo_alumnos_upper)

if sexo_alumnos_upper == "F" and nombre_alumnos_lower < "m":
    print("La persona pertenece al grupo A")
elif sexo_alumnos_upper == "M" and nombre_alumnos_lower > "n":
    print("La persona pertenece al grupo A")
else:
    print("La persona pertenece al grupo B")
"""


### --------------------------------- DESAFIOS EJERCICIOS CONDICIONALES
"""
DESAFIO 1:
En nuestro rol de Devs (Programador o Programadora de Software), debemos elaborar un programa en Python que
permita emitir un mensaje de acuerdo a lo que una persona ingresa como cantidad de años que viene usando 
insecticida en su plantación. 
Si hace 10 o más añoss, debemos emitir el mensaje "Por favor solicite revisión de suelos en su plantación". 
Si hace menos de 10 años, debemos emitir el mensaje 
"Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación".
"""
"""
print("Hola. Mucho gusto, ")
años_insecticida = int(input("Cuantos años hace que usa insecticida en sus plantaciones?: "))
if años_insecticida >= 10:
    print("Por favor solicite revision de sueles en sus plantaciones.")
else:
    print("Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación.")
"""


"""
---------------------------------  DESAFIO 2:
Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores un programa en Python
que dado el tamaño de un pez indique si su organismo está contaminado. Para ello tendremos 4 opciones:
Tamaño Normal: Mensaje "Pez en buenas condiciones"
Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
Tamaño sobredimensionado: Mensaje "Pez contaminado"

"""

"""
print ("Mucho gusto!!! Identifique el tamaño del pez, por favor!")

print ("A: Tamaño normal")
print ("B: Por debajo de lo normal")
print ("C: Un poco por encima de lo normal")
print ("D: Sobredimensionado")


tamaño_pez = input("Elija una de las opciones visualizadas (A, B, C, D): ")

if tamaño_pez.lower() == "a":
    print ("Pez en buenas condiciones!")
elif tamaño_pez.lower() == "b":
    print ("Pez con problemas de nutrición")
elif tamaño_pez.lower() == "c":
    print ("Pez con síntomas de organismo contaminado")
elif tamaño_pez.lower() == "d":
    print ("Pez contaminado")

while tamaño_pez.lower() > "d":
    
    tamaño_pez = input("Elija una de las opciones visualizadas (A, B, C, D): ")

    if tamaño_pez.lower() == "a":
        print ("Pez en buenas condiciones!")
    elif tamaño_pez.lower() == "b":
        print ("Pez con problemas de nutrición")
    elif tamaño_pez.lower() == "c":
        print ("Pez con síntomas de organismo contaminado")
    elif tamaño_pez.lower() == "d":
        print ("Pez contaminado")
"""

"""
---------------------------------  Desafío 3
Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el suelo el 
cual debe existir en una cantidad de al menos 10% por hectárea, y no debe existir vegetación del tipo MATORRAL.
Escribir un programa que determine si es factible la utilización de fertilizantes.
"""

"""
print("¡Mucho gusto! Vamos a determinar si es factible la utilización de fertilizantes.")
compuesto_utilizado = float(input("Determinar el porcentaje de compuesto por hectarea: "))
vegetacion = input("Que tipo de vegetacion existe en la hectarea: ")

if compuesto_utilizado>=10 and vegetacion.lower() != "Matorral":
    print("Es factible la utilización de fertilizantes.")
else:
    print("No es factible la utilización de fertilizantes.") 
"""    


"""
---------------------------------  DESAFÍO 4
Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.

Ingredientes comunes: Verduras y berenjena.
Ingredientes Receta 1: Lentejas y apio.
Ingredientes Receta 2: Morrón y Cebolla..

Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta le muestre un menú 
con los ingredientes disponibles para que elija. Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) y el tipo de receta. 
Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes.

"""
"""
print("Vamos a cocinarle:")
a = "a) receta1"
b = "b) receta2"
receta1 = "Ingredientes Receta 1: Lentejas y apio."
receta2 = "Ingredientes Receta 2: Morrón y Cebolla.."
ingredientes_comunes = "Ingredientes comunes: Verduras y berenjena."
ingrediente_comun1 = "1) Verduras"
ingrediente_comun2 = "2) berenjena"

print(a)
print(b)

receta_elegida = input("Elija la receta a realizar: ")

if receta_elegida.lower() == "a":
    print("Elija que ingredientes comunes va a utilizar: ")
    print(ingrediente_comun1)
    print(ingrediente_comun2)
    terceringrediente=int(input("Ingrese el 3er ingrediente que le añadira (1 o 2): "))
    if terceringrediente == 1:
        print("Los ingredientes a utilizar son Lentejas, Apio y Verduras")
    else:
        print("Los ingredientes a utilizar son Lentejas, Apio y berenjena.")

if receta_elegida.lower() == "b":
    print("Elija que ingredientes comunes va a utilizar: ")
    print(ingrediente_comun1)
    print(ingrediente_comun2)
    terceringrediente=int(input("Ingrese el 3er ingrediente que le añadira (1 o 2): "))
    if terceringrediente == 1:
        print("Los ingredientes a utilizar son Morron, Cebolla y Verduras")
    else:
        print("Los ingredientes a utilizar son Morron, Cebolla y berenjena.")
        
"""    


"""
---------------------------------  DESAFÍO 5
La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre del barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)
La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y 
los barrios no céntricos con nombre posterior a la M, y la sección B el resto.
Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra.
"""

print("Mucho gusto, averiguaremos la seccion en la que se encuentra.")
print("Tipos de barrios: ")
print("centrico")
print("no centrico")

barrio = input("Ingresar el nombre del barrio en el que se encuentra: ")
ubicacion = input("Ingresar el tipo de barrio en el que se encuentra: ")
# Python ordena el abecedario de izquiera a derecha, es decir "A" es mayor a "M".

if ubicacion.lower() == "centrico" and barrio.lower()>="M":
    print("Seccion A.")
elif ubicacion.lower() == "no centrico" and barrio.lower()<="M":
    print("Seccion A.")
else:
    print("Seccion B.")