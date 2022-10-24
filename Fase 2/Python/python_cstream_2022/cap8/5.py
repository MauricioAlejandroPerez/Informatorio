#def get_max(numbers):
#    try:
#        r = numbers[0]
#        for num in numbers:
#            if num > r:
#                r = num
#        return r
#    except IndexError:
#        return None

def get_max(numbers):
    if len(numbers) > 0:
        r = numbers[0]
        for num in numbers:
            if num > r:
                r = num
        return r
    else:
        return None
   
print(get_max([0, -10, 200, 3405, 7, 1020, 77, 22, 156, 2]))
print(get_max([]))

# definir una function que reciba una lista de numeros 
# y ordernarlos de menor a mayor 

def ordenar_lista(numbers):
    #magic here
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1 # j 0
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j = j - 1
        numbers[j + 1] = key
    return numbers
    #[0, -10  , 200, 3405, 7, 1020, 77, 22, 156, 2]
    #      i               i = 4
    #     key = -10        j = 2
    #     0
    # -10 0, 200, 3405 
    # -10, 0, 7, 200, 3405, ....  
 

a = ordenar_lista([0, -10, 200, 3405, 7, 1020, 77, 22, 156, 2])
print(a)


# definir una function que determine si un numero ingresado es primo
# 
def is_prime(num):
    # magic here
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(15))

def list_primes_upto(num):
    for i in range(2, num):
        if is_prime(i):
            print(f"{i} is prime!")

list_primes_upto(1000)


# definir una funcion que reciba un string y determine si es un palindromo

# Ejemplos:
"""
arenera
asa
radar
reconocer
rotor
"""

def palindromo(param):
    i = 0
    j = len(param) - 1
    mid = len(param)//2
    while i < mid:
        if param[i] == param[j]:
            j = j - 1
            i += 1
        else:
            break
    if i == mid:
        return True
    return False

def palindromo2(param):
    if param == param[::-1]:
        return True
    return False
    
print(palindromo2("neuquena"))

