
# Hacer un programa que acepte valores por teclado del usuario
# convertir estos valores a numeros (de ser posible) y sumarlos a todos
# El programa termina cuando el input sea igual a 'quit'. En este caso,
# Mostrar el resultado de la sumatoria hasta ese momento y terminar. 
# ( Combinar input() y while() )

sumatoria = 0
while True:
    print('Ingrese nuevo valor o "quit"')
    user_num = input()
    if user_num == 'quit':
        break
    sumatoria = sumatoria + int(user_num)

print(f'Sumatoria final = {sumatoria}')