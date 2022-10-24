'''
Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo.
'''
palabra = (input("Ingrese una palabra para determinar si es palindromo: ")).lower()

lista_palabra = list(palabra)

if lista_palabra == lista_palabra[::-1]:
    print("\nLa palabra es palindromo")
else:
    print("\nLa palabra no es palindromo")
