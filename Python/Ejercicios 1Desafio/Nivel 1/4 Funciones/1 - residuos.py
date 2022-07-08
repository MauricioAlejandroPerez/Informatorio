'''
150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede 
tardar 1.000 años en desaparecer. 

Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.

Un trozo de chicle tarda 5 años en degradarse. 

Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, 
botella PET, envase tetrabrik o chicle, e imprima la cantidad de años que tarda en degradarse.
'''
# Variables:
residuos = {
        "Bolsa de plastico" : 150,
        "Botella PET" : 1000,
        "Envase de Tetrabrik" : 30,
        "Chicle" : 5
}

def tacho():
    residuos_enumerados = {}
    contador = 0
    print("Que residuo desea desechar? ")
    for k, v in residuos.items(): # Enumerando los items del diccionario
            contador += 1
            print(f"{contador}. {k}.")
            residuos_enumerados[contador] = v 
    tirar = int(input(""))

    return print(f"Este residuo tardara en degradarse {residuos_enumerados[tirar]} anios.")

tacho()