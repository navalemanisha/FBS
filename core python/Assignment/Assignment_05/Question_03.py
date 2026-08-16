n = int(input("Enter number of passengers: "))
cost = float(input("Enter ticket cost: "))

total = 0

for i in range(n):
    age = int(input("Enter age of passenger: "))

    if age < 12:
        amount = cost - (cost * 30 / 100)
    elif age > 59:
        amount = cost - (cost * 50 / 100)
    else:
        amount = cost

    total = total + amount

print("Total ticket amount =", total)