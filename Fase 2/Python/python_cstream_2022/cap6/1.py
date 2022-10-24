persona = {

        "nombre": "John",
        "edad"  : 28,
        "sexo"  : "fluido"
}


#personas = [
#    {
#        "nombre": "John",
#        "edad"  : 28,
#        "sexo"  : "fluido"
#    },
#
#     {
#        "nombre": "Marta",
#        "edad"  : 22,
#        "sexo"  : "delfin"
#    },
#]

#print(f'nombre de la persona: {persona["nombre"]}')

#print(persona["edad"])
#print(persona["sexo"])

for k, v in persona.items():
    print(k, v)

for k in persona.keys():
    print(k)