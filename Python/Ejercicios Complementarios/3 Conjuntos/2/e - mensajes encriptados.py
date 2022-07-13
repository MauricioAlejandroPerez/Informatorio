'''
 Se tiene una lista que contiene mensajes encriptados de varios usuarios. Cada mensaje se encierra entre {}, 
 y para indicar que se terminó el área de mensajes de un usuario se usa un signo &. Indique cuántos usuarios 
 y cuántos mensajes hay en la lista, teniendo en cuenta que todos los mensajes están correctamente formados, 
 es decir comienzan con { y terminan con }. Y que es seguro que al menos exista un usuario en la lista
'''
lista = ["mensaje {encriptado}&", "}no un& mensaje{", "{encriptados}&"]
contador = 0

for mensaje in lista:
    if mensaje.startswith("{") and mensaje.endswith("}&"):
        contador += 1

print(f"La lista contiene {contador} mensajes encriptados")