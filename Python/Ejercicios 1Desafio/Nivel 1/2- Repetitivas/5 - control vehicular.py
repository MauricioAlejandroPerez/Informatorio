'''
Se está desarrollando un sistema de control de vehículos desde donde se han tirado restos 
de basura a la vía pública.

Para ello la ciudad cuenta con sistemas de monitoreo de patentes que devuelve 3 letras y 
un valor numérico de 5 dígitos a la Central con el siguiente significado:

3 letras: Correspondientes a la patente.
Del valor numérico:
Los 3 primeros números corresponden a la patente

El 4 número indica
1- Tiró basura a la vía pública
0 - No tiró basura a la vía pública

El 5 número indica
1- Ya había sido multado el vehículo
0 - Vehículo sin multas.

Deberás informar cantidad de vehículos observados, cantidad de vehículos que han tirado basura 
y porcentaje de éstos que ya habían sido multados.
'''
# Variables:
vehiculos = 0
tiro_basura =0 
fue_multado = 0
patente = ""

# Programa:
while patente != "quit":
    patente = input("Ingrese la patente del vehiculo sin espacios ('quit' para finalizar):\n")
    if patente == "quit":
        break
    else:
        vehiculos += 1 

        patente += input("Este vehiculo arrojo basura a la via publica?:\
                        \n0 - No tiró basura a la vía pública.\
                        \n1 - Tiró basura a la vía pública.\n")

        patente += input("Este vehiculo ya habia sido multado?:\
                        \n0 - Vehículo sin multas.\
                        \n1 - Ya había sido multado el vehículo.\n")

        if patente[6] == "1":
            tiro_basura += 1
            if patente[7] == "1":
                fue_multado += 1

# Resultados:
print(f"Han sido observados {vehiculos} vehiculos.")
print(f"Entre ellos {tiro_basura} han arrojado basura a la via publica.")
print(f"De estos, el {(fue_multado / tiro_basura * 100):.2f}% ya habia sido multado con anterioridad.")