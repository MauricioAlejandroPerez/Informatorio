# Lista (mutable)
mi_lista = [1,2,3,4,5]

# Tuple (inmutable)
mi_tupla = (1,2,3,4,5)
print(mi_tupla[0])
# mi_tupla[0] = 1 # esto falla

new_list = list(mi_tupla)
print(new_list, type(new_list))