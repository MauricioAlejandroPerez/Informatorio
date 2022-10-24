'''
5- 
Escribir un programa que pregunte al usuario la fecha de su 
nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, 
el mes y el año. Adaptar el programa anterior para que también 
funcione cuando el día o el mes se introduzcan con un solo carácter.

Solucion:


'''

Date = input("Introduzca su fecha de nacimiento: \n").split("/")

print(f"Ud. nacio el dia {int(Date[0]):02d}. \
        \nDel mes {int(Date[1]):02d}.\
        \nDel año {int(Date[2]):04d}.")