import random

#r = random(0, 100)

i = 0
while True:
    r = random.randint(0, 1000000)
    if r == 49:
        print(f"magic number found at iteration: {i}")
        break
    i += 1

