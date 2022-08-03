'''
En una jurisdicción particular, las matrículas más antiguas consisten en tres letras seguidas de tres números. 
Cuando se utilizaron todas las placas que siguen ese patrón, el formato se cambió a cuatro números seguidos de 
tres letras. Escriba una función que genere una matrícula aleatoria. Escriba un programa principal que llame a 
su función y muestre la placa generada al azar.
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Bulldog(Dog):
    pass

jack = Bulldog("Jack", 12)

print(isinstance(jack, Dog))