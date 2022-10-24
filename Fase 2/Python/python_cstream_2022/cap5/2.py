cars = ['audi', 'bmw', 'subaru', 'toyota']

for i in range(len(cars)):
    if cars[i] == 'bmw':
        print(f"Iteration {i}: {cars[i].upper()}")
    else:
        print(f"Iteration {i}: {cars[i].title()}")