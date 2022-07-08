'''
En una jurisdicción particular, las tarifas de taxi consisten en una tarifa base de $40.00, más $15.00 por 
cada 140 metros recorridos. Escriba una función que tome la distancia recorrida (en kilómetros) como su único 
parámetro y devuelva la tarifa total como su único resultado. Escriba un programa principal que use la función.

Sugerencia: Utilice constantes para presentar la base y la porción variable de las tarifas así el programa podrá 
actualizar fácilmente cuando las tasas aumentan.
'''
tarifa_base = 40
extra = 15

taquimetro = lambda km_recorrido : tarifa_base + extra * round(km_recorrido * 1000 / 140)

km_recorrido = float(input("Cuantos Km lo transporto el taxi? "))

print(f"El costo del taxi es de $ {taquimetro(km_recorrido):.2f}.\
        \nPor los {km_recorrido:.2f} Kms. recorridos en taxi.")
        