import random

for i in range(100):
    num = random.randint(0,1000)
    if num == 42:
        print(f"Se encontro la respuesta en la iteracion {i}")
        break
    elif num == 43 or num == 41:
        print(f"casi se encontro la respuesta en la iteracion: {i}")
    #else:
    #    print(f"en la iteracion {i} no hay nada")