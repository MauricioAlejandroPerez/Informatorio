'''
Escribir un programa que cargue una tupla con nombres de especie, y para cada nombre de especie imprima 
el mensaje Hola soy ......, cuidame.

Modificá el programa anterior y dada una posición inicial p y una cantidad n, imprima el mensaje anterior 
para los n nombres que se encuentran a partir de la posición i.
'''
especies = ("tucan", "yaguarete", "politico honesto", "dorado")

# for i in especies:
#     print(f"Hola soy un {i}, cuidame.")

p = int(input(f"Ingrese una posicion empezando por entre 1 y {len(especies)}: ")) - 1

for i in range(p, len(especies)):
    print(f"Hola soy un {especies[i]}, cuidame.")

