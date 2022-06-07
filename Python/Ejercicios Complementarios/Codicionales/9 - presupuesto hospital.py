'''
En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y Kinesiología. 
El presupuesto anual del hospital se reparte conforme a la sig. tabla:

ÁREA 		  PORCENTAJE

Pediatría		 60%

Traumatología	 20%

Kinesiología	 20%


Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal 		
que se ingrese por teclado.
'''
presupuesto = float(input("Ingrese el monto de presupuesto total:\n"))

print(f"El presupuesto total es de ${presupuesto:.2f}")
print(f"Del total se distribuira de la siguiente manera en las distintas areas:\n")
print(f"AREA\t     PORCENTAJE\t  MONTO")
print(f"Pediatria\t60%\t${(presupuesto * .6):.2f}")
print(f"Traumatologia\t20%\t${(presupuesto * .2):.2f}")
print(f"Kinesiologia\t20%\t${(presupuesto * .2):.2f}")