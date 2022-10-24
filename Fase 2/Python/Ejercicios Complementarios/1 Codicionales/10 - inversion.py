'''
Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad 
distinta. Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida.
'''
inversor_1 = float(input("Ingrese el monto del capital invertido por el primer inversor:\n"))
inversor_2 = float(input("Ingrese el monto del capital invertido por el segundo inversor:\n"))
inversor_3 = float(input("Ingrese el monto del capital invertido por el tercer inversor:\n"))

total_invertido = inversor_1 + inversor_2 + inversor_3

print(f"El total invertido es de ${total_invertido:.2f}.\
      \nEl primer inversor tiene una participacion del {(inversor_1 / total_invertido * 100):.2f}%.\
      \nEl segundo inversor tiene una participacion del {(inversor_2 / total_invertido * 100):.2f}%.\
      \nEl tercer inversor tiene una participacion del {(inversor_3 / total_invertido * 100):.2f}%.")