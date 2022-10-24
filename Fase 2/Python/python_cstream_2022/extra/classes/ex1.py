
import time
import random

#def saludar(nombre):
#    print(f"Hola {nombre}")


#saludar("Mauri")

class Mascota:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad   = edad
    
    def __str__(self):
        desc = f"{self.nombre} - {self.edad}"
        return desc

    def jugar(self):
        print("Juega como animal desconocido")


class Gato(Mascota):

    def jugar(self):
        print("romper sillon")


class Perro(Mascota):
    
    def jugar(self):
        print("pasear con huesito")




class Persona:

    # variables de clase

    # metodos de clase
    def __init__(self, nombre, edad=18):
        self.nombre = nombre.title()
        self.edad = edad
        self.mascotas = []

    def __str__(self):
        desc = f"Persona: {self.nombre} - {self.edad}\n"
        for mascota in self.mascotas:
            desc += f"  {str(mascota)}\n"
        return desc

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def pasear_mascota(self):
        if len(self.mascotas) > 0:
            mascota_con_suerte = random.choice(self.mascotas)
            print(f" - {self.nombre} va a pasear a {mascota_con_suerte.nombre}:")
            mascota_con_suerte.jugar()
            time.sleep(2)
    

mauri = Persona("mauri", edad=30)
gisse = Persona("gisse", edad=31)
juan  = Persona("juan")


chiqui = Perro("chiqui", 15)
freya  = Gato("freya", 5)
popis  = Mascota("popis", 5)
mulan  = Perro("mulan", 3)
kira   = Gato("kira", 3)

gisse.agregar_mascota(chiqui)
gisse.agregar_mascota(popis)
gisse.agregar_mascota(kira)


mauri.agregar_mascota(mulan)
mauri.agregar_mascota(freya)

print(mauri)
print(gisse)
print(juan)


personas_con_mascota = [mauri, gisse]

for i in range(10):
    p = random.choice(personas_con_mascota)
    p.pasear_mascota()