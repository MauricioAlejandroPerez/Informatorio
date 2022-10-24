import time

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

user_topping = input("Extra topping?: ")
requested_toppings.append(user_topping)

added_toppings = []

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        added_toppings.append(requested_topping)
        print(f"Adding {requested_topping}.")

print("\n - We're preparing your pizza now!")
time.sleep(5)

topping_msg = "" # mushrooms, extra cheese, anchoas

for i in range(len(added_toppings)):
    if i == len(added_toppings) - 1:
        topping_msg = topping_msg + f"{added_toppings[i]}"
    else:
        topping_msg = topping_msg + f"{added_toppings[i]}, " 
        # topping_msg = "mushrooms, " + "extra cheese, "
#topping_msg = topping_msg[:-2]

print(f"\n --> Finished making your pizza with {topping_msg}!")