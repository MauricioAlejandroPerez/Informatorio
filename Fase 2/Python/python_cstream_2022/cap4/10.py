motorcycles = ['honda', 'yamaha', 'suzuki']

my_list = []    
for bike in motorcycles:
    my_list.append(bike.upper())

print(my_list)

motorcycles_upper = ([bike.upper() for bike in motorcycles])

print(motorcycles_upper)