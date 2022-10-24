pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while len(pets) > 0:
    print(f"Pet: {pets[0]}")
    pets.pop(0)
 
print(pets)