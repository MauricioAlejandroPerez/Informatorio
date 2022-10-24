alien = {
    "color": "green",
    "points": 5,
}

# add key
alien["rayos-x"] = True

for k, v in alien.items():
    print(k, v)

print("===============================")
# delete key
del alien["rayos-x"]

for k, v in alien.items():
    print(k, v)

print("===============================")

alien["color"] = "red"

for k, v in alien.items():
    print(k, v)