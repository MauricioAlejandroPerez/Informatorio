'''
Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10, 
almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor. 
'''
cuanto_conoce = []
valor_error = "\nValor ingresado incorrecto.\nIntente nuevamente."

while True:
    num = int(input("Del 1 al 10, cuanto conoce sobre contaminacion? (0 para salir) "))
    
    if num == 0:
        break
    elif num < 0 or num > 10:
        print(valor_error)
        continue
    
    cuanto_conoce.append(num)
    cuanto_conoce.sort()

print(cuanto_conoce)