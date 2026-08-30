# 4. Sum of all odd numbers between 1 to n

# 1. Without Parameter, Without Return Value
def odd_sum():
    n = int(input("Enter n: "))
    total = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i

    print("Sum =", total)

odd_sum()

# 2. With Parameter, With Return Value
def odd_sum(n):
    total = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i

    return total

n = int(input("Enter n: "))
result = odd_sum(n)
print("Sum =", result)


# 3. Without Parameter, With Return Value
def odd_sum():
    n = int(input("Enter n: "))
    total = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i

    return total

result = odd_sum()
print("Sum =", result)

# 4. With Parameter, Without Return Value
def odd_sum(n):
    total = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i

    print("Sum =", total)

n = int(input("Enter n: "))
odd_sum(n)

