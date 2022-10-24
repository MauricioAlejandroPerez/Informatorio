import random

#r = random(0, 100)

r = random.randint(0, 1000000)
i = 0
while r != 49:
    r = random.randint(0, 1000000)
    i += 1

if r == 49:
    print(f"magic number found at iteration: {i}")
