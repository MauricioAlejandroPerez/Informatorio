'''
x = list(range(5))

for num in x:
    print(num)
'''
'''
listType = ['US', 'UK', 'India', 'China']
for i in range(len(listType)):
    print(listType[i])

my_list = [7, 4, 3, 4, 5]
'''
'''
my_list = list([7,6,3,4,5])
my_list.insert(3, 'test')
print(my_list)
# Ahora el valor de la lista es [7, 6, 3, 'test', 4, 5]
'''
'''
my_list = [7, 4, 3, 4, 4, 5]

my_list.remove(4) # removera el primer valor indicado

print(my_list)
# Print: [7, 3, 4, 4, 5]
'''
'''
my_list = ['z', 'x', 'm', 'r', 'b']

my_list.pop(2) # remueve la posicion indicada

print(my_list)
# Print: ['z', 'x', 'r', 'b']
my_list.pop() # si no se indica remueve la ultima posicion de la lista

print(my_list)
# Print: ['z', 'x', 'r']
'''
'''
# suma de listas, tambien se puede multiplicar una lista
my_list = ['x']
my_list2 = ['m', 'c', 'r']
my_list3 = my_list + my_list2
print(my_list3)
# Print: ['x', 'm', 'c', 'r']
'''
'''
# invertir una lista
my_list = [1, 2, 3, 4, 5]
my_list_reversed = my_list[::-1]
print(my_list_reversed)
# Print: [5, 4, 3, 2, 1]
'''
'''
# vaciar una lista
my_list = [2,1,5,4,3]
my_list.clear()
print(my_list)
# Print: []
'''
'''
squares = [value**2 for value in range(1, 11)]
print(squares)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lista = [value for value in range(1,11)]
# o tambien: 
# lista = list(range(1,11)) 
print(lista)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)