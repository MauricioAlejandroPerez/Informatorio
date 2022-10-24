'''
Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles plantados en 
diferentes ciudades de Argentina durante la cuarentena. Luego la función debe devolver dos listas ordenadas. 
La primera con las cantidades que superen los 100 y la segunda con el resto.

Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.
'''
arboles_plantados = [ {"Resistencia": 123}, {"Corrientes": 59}, {"La Plata": 433}, {"Santiago del Estero": 20}]

def separar(lista):
    ciudades = [k for dic in lista for k, v in dic.items()] 
    arboles = [v for dic in lista for k, v in dic.items()] 

    print("Ciudades que han plantado mas de 100 arboles durante la cuarentena")
    for i, arbol in enumerate(arboles):
        if arbol > 100:
            print(ciudades[i], arbol)

    print("Ciudades que han plantado 100 arboles, o menos, durante la cuarentena")
    for i, arbol in enumerate(arboles):
        if arbol <= 100:
            print(ciudades[i], arbol)

separar(arboles_plantados)
