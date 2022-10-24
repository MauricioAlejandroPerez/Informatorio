first_name = "ada"
last_name = "lovelace"
age       = 32
# formatting python 3.6+
full_name = f"{first_name} {last_name} is {age}"
print(full_name)

# formatting python < 3.6
full_name2 = "{} {} is {}".format(first_name, last_name, age)
print(full_name2)