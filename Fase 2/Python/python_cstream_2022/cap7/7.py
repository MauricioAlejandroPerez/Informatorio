pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
i = 0
while 'cat' in pets:
    print(f"removing cat {i}")
    pets.remove('cat')
    i += 1
 
print(pets)