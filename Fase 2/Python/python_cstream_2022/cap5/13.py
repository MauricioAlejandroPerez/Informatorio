age = 15

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
elif age == 16:
    print("sweet 16")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    if age == 16:
        print("sweet 16")
    else:
        print("Sorry, you are too young to vote.")
        print("Please register to vote as soon as you turn 18!")