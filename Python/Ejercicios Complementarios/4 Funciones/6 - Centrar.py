'''
Escriba una función que tome una cadena de caracteres como primer parámetro y el ancho de la terminal en 
caracteres como segundo parámetro. Su función debe devolver una nueva cadena que consta de la cadena 
original y el número correcto de espacios iniciales para que la cadena original aparezca centrada dentro 
del ancho proporcionado cuando se imprima. No agregue ningún carácter al final de la cadena. Incluya un 
programa principal que use su función.
'''
# Largo del terminal: 153 caracteres
def centrar_titulo(titulo):
    espaciado = " " * round((153 - len(titulo)) / 2)
    print(espaciado + titulo)

titulo = input("Ingrese un titulo: ")

centrar_titulo(titulo)