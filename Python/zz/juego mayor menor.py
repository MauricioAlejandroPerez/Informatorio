import random


numero = random.randint(1, 100)
intento = 0

print("Estoy pensando en un numero del 1 al 100"
    "\nIntente adivinarlo en la menor cantidad de intentos posibles")
while True:
    intento += 1
    adv = int(input("En que numero crees que estoy pensando?\n"))
    
    if adv > numero:
        print("Fallaste! El numero en el que estoy pensando es MENOR."
            "\nIntenta otra vez!")
    elif adv < numero:
        print("Fallaste! El numero en el que estoy pensando es MAYOR."
            "\nIntenta otra vez!")
    else:
        print(f"Acertaste! El numero en el que estaba pensando es el {numero}.")
        break

print(f"Solo te tomo {intento} intentos.")