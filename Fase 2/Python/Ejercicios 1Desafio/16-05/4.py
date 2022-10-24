'''
4- 
Escribir un programa que pregunte el correo electrónico del 
usuario en la consola y muestre por pantalla otro correo 
electrónico con el mismo nombre (la parte delante de la arroba @) 
pero con dominio com.ar


'''
email = input("Ingrese su correo electronico: \n")
dominio = ""

# for letter in email:
#         if letter != "@":
#                 dominio = dominio + letter
#         else: break

dominio = email.split("@")

print(dominio[0] + ".com.ar")

