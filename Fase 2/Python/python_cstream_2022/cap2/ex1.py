PROT_PER_KG = 0.8
KG_TO_POUND = 2.2046

peso_kg = float (input ("Ingrese su peso en kg: "))

peso_pd = peso_kg * KG_TO_POUND

prot_per_kg = peso_pd * PROT_PER_KG

msg2 = "Para "+ str(peso_kg)  +" cantidad de kg, se debe consumir "+ str(prot_per_kg) +" cantidad de proteina"


print (msg2)
print ("Usted debe ingerir %.2f proteinas diarias" % prot_per_kg)
print ("Usted debe ingerir {:.2f} proteinas diarias".format(prot_per_kg))
print (f"Para {peso_kg} cantidad de kg, usted debe ingerir {prot_per_kg:.2f} proteinas diarias")