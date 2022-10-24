'''
En este ejercicio creará una función llamada proximo_primo que encuentra y devuelve el primer número primo mayor 
que algún número entero, n. El valor de n se pasará a la función como su único parámetro. Incluya un programa 
principal que lea un número entero del usuario y muestre el primer número primo mayor que el valor ingresado.
'''
def es_primo(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True

def proximo_primo(num):
    for i in range(num + 1, num + 100):
        if es_primo(i):
            return i

print(proximo_primo(1000003))

#proxprim = lambda num: i if es_primo(i) for i in range(num, num + 100)