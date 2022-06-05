list1 , list2 = [] , []
max_range = 2
count = 0

for i in range(max_range):
    customer_name = input("Customer name: ")
    list1.append(customer_name)

    spent = float(input("Amount Spent: "))
    list2.append(spent)

    count += spent
    averageSpent = count / max_range

print("Name\t\t\tAmount")
for i in range(len(list1)):
    print(f'{list1[i]} \t\t\t$ {list2[i]}')
print("Total spending:\t\t $", count)
print("Average spending:\t $", averageSpent)

print("Most money spent:\t $", max(list2))
print("Least money spent:\t $", min(list2))