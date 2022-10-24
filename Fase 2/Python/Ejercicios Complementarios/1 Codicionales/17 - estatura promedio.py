'''
Determinar y exhibir si la estatura de una persona adulta dada, es mayor que la estatura media 
de las personas adultas de su sexo, siendo:

- estatura media de mujeres adultas: 1,65 m.

- estatura media de varones adultos: 1,72 m.
'''
sexo = input("Por favor indique su sexo (F/M): ").lower()
estaura = float(input("Por favor introduzca su estatura: "))

if sexo == "m":
    if estaura < 1.72:
        media ="INFERIOR"
    elif estaura > 1.72:
        media ="SUPERIOR"
    elif estaura == 1.72:
        media ="IGUAL"
    print(f"Su estatura es {media} a la media para una persona de sexo masculino de su edad.")
elif sexo == "f":
    if estaura < 1.72:
        media ="INFERIOR"
    elif estaura > 1.72:
        media ="SUPERIOR"
    elif estaura == 1.72:
        media ="IGUAL"
    print(f"Su estatura es {media} a la media para una persona de sexo demenino de su edad.")
else:
    print("El valor ingresado es incorrecto.")