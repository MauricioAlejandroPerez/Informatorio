'''
Leer una frase y luego invierta el orden de las palabras en la frase. Por Ejemplo: 
“una imagen vale por mil palabras” debe convertirse en “palabras mil por vale imagen una”.
'''
frase = "una imagen vale por mil palabras"

frase_listada = frase.split(" ") 

# for palabra in frase_listada[::-1]:
    # print(palabra, end= " ")

print(" ".join(frase_listada[::-1]))