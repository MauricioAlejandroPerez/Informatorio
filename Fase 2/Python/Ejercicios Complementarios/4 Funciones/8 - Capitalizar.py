'''
Muchas personas no usan letras mayúsculas correctamente, especialmente cuando escriben en dispositivos pequeños como 
teléfonos inteligentes. En este ejercicio, escribirá una función que capitaliza los caracteres apropiados en una cadena. 
Una "i" minúscula debe reemplazarse por una "I" mayúscula si está precedida y seguida de un espacio. El primer carácter 
de la cadena también debe estar en mayúscula, así como el primer carácter no espacial después de un ".", "!" o "?". 
Por ejemplo, si la función se proporciona con la cadena "¿a qué hora tengo que estar allí? ¿cuál es la dirección?" 
Entonces debería devolver la cadena "¿A qué hora tengo que estar allí? ¿Cuál es la dirección?". 
Incluya un programa principal que lea una cadena del usuario, la capitalice utilizando su función y muestre el resultado.
'''
def capitalizador(texto):
    texto = texto.capitalize()
    nuevo_string = ""

    for i, letter in enumerate(texto):
        if texto[i - 1] == "¡" or texto[i - 1] == "¿":
            nuevo_string += letter.upper()
        elif i > 1 and (texto[i - 2] == "." or texto[i - 2] == "!" or texto[i - 2] == "?"):
            nuevo_string += letter.upper()
        else:
            nuevo_string += letter

    return nuevo_string 

cadena = capitalizador(input("Escriba un mensaje: "))

print(cadena)