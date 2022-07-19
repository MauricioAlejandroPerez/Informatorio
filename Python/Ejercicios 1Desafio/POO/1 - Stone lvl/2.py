'''
> Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos.

> Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra 
  mostrando el nombre de su clase y sus atributos.

> Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo 
  que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. 
  También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente 
  si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.

Nota
Puedes utilizar el atributo especial de clase name para recuperar el nombre de la clase de un objeto:
type(objeto).__name__
.                         ______________
.                        | |Vehiculos| | 
.                        |   Color,    |
.                        |  Ruedas     |
.                        --------------
.                            /\ /\                      
.         ___________________|  |__________________
 ________|__________                   ___________|____________ 
|     |Coche|      |                  |     |Bicicleta|       |
| Velocidad (Km/h),|                  |tipo (urbana/deportiva)|
| Cilindrada (cc)  |                  ------------------------
-------------------                            /\ 
.      /\                                      | 
.______|_______                        ________|__________
| |Camioneta| |                       |   |Motocicleta|  |
| Carga (kg)  |                       | Velocidad (Km/h),|
--------------                        | Cilindrada (cc)  |
.                                     -------------------
'''