import random

my_list = []

for i in range(0,10):
    my_list.append(random.randint(0, 100))

print(my_list)

sumatoria1 = 0
for val in my_list:
    sumatoria1 = sumatoria1 + val

print(sumatoria1)

sumatoria2 = 0
for i in range(0, len(my_list)):
    sumatoria2 = sumatoria2 + my_list[i]

print(sumatoria2)

print( sumatoria1 == sumatoria2 )