'''
3- 
Una frutería vende el kg de manzanas a $300. 
La fruta que no es el día tiene un descuento del 50%. 
Escribir un programa que comience leyendo el número de 
kg vendidos que no son del día. Después el programa 
debe mostrar el precio habitual de 1kg de manzana, el 
descuento que se le hace por no ser fresca y el costo final total.

Solución:

'''
ManzanaVieja = float(input("Cuantos Kgs. de manzanas que no son del dia se vendieron? \n"))
ManzanaPrecio = 300
DescuentoManzana = .5
TotalAPagar = ManzanaVieja * ManzanaPrecio * DescuentoManzana

print("El precio habitual por kilo de manzana del dia es de $300.")
print(f"Se le aplica un descuento del {DescuentoManzana:.2%} a la fruta que no es el dia.")
print(f"Debera abonar ${TotalAPagar:.2f} por {ManzanaVieja:.2f} Kgs. de Manzana en oferta.")