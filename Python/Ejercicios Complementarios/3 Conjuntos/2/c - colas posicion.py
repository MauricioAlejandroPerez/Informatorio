'''
Simular la operación de colas de un Rapipago, que funciona con dos colas diferentes. El usuario llega 
y se ubica en la cola de menor cantidad de personas. Al finalizar el proceso indique cuántos elementos 
tiene cada cola.
'''
cola1 = []
cola2 = []

while input("Presione 'Enter' para posicionarse en la cola mas corta.") == "":
    
    if len(cola1) < len(cola2):
        cola1.append(1)
        print(f"Ud. se encuentra en la cola 1, en la posicion {len(cola1)}")
    else:
        cola2.append(1)
        print(f"Ud. se encuentra en la cola 2, en la posicion {len(cola2)}")

print("Cola uno: ") 
print(cola1)
print("Cola dos: ")
print(cola2)