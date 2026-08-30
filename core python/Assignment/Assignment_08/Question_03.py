# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n


# 1. Without passing Parameter, Without Return Value
def sum_series():
    n = int(input("Enter n: "))
    total = 0

    for i in range(1, n + 1):
        total += i

    print("Sum =", total)

sum_series()

# 2. With passing Parameter, With Return Value
def sum_series(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

n = int(input("Enter n: "))
result = sum_series(n)
print("Sum =", result)

# 3. Without passing Parameter, With Return Value
def sum_series():
    n = int(input("Enter n: "))
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

result = sum_series()
print("Sum =", result)


# 4. With passing Parameter, Without Return Value
def sum_series(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    print("Sum =", total)

n = int(input("Enter n: "))
sum_series(n)