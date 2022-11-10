'''
Escriba una función que tome tres números como parámetros y devuelva el valor medio de esos parámetros como resultado. 
Incluya un programa principal que lea tres valores del usuario y muestre su mediana.

Sugerencia: El valor medio es el medio de los tres valores cuando se ordenan en orden ascendente. Se puede encontrar 
usando declaraciones if, o con un poco de creatividad matemática.
'''
# def mediana(v1, v2, v3):
#     if v3 <= v1 <= v2 or v2 <= v1 <= v3:
#         valor_medio = v1
#     elif v3 <= v2 <= v1 or v1 <= v2 <= v3:
#         valor_medio = v2
#     elif v1 <= v3 <= v2 or v2 <= v3 <= v1:
#         valor_medio = v3
#     return valor_medio

def mediana(lista):
    # lista = [v1, v2, v3]
    lista.remove(min(lista))
    lista.remove(max(lista))
    valor_medio = lista[0]
    return valor_medio

lista_valores = []
while len(lista_valores) < 3: 
    lista_valores.append(int(input("Ingrese un valor entero: ")))
# v2 = int(input("Ingrese un valor entero: "))
# v3 = int(input("Ingrese un valor entero: "))

print(f"El valor de la mediana es: {mediana(lista_valores)}")