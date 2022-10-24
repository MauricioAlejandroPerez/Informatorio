def suma(a , b):
    r = a + b
    return r

def mul(a, b):
    r = a * b
    return r

def resta(a, b):
    r = a - b
    return r

def div(a, b):
    if b == 0:
        print("you dirty boy... mothefucker")
        return -1
    r = a//b
    return r

def print_operations():
    print("Que operacion realizar?")
    print("1. suma")
    print("2. multiplication")
    print("3. resta")
    print("4. division")

while(True):
    valor_a = int(input("a: "))
    valor_b = int(input("b: "))
    print_operations()
    op = input("Opcion: ")
    if op == "1":
        res = suma(valor_a, valor_b)
    elif op == "2":
        res = mul(valor_a, valor_b)
    elif op == "3":
        res = resta(valor_a, valor_b)
    if op == "4":
        res = div(valor_a, valor_b)
    print(f"resultado: {res}")

