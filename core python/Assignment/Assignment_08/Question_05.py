# 5. Sum of all prime numbers between 1 to n


# 1. Without Parameter, Without Return Value
def prime_sum():
    n = int(input("Enter n: "))
    total = 0

    for num in range(2, n + 1):
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count == 2:
            total += num

    print("Sum =", total)

prime_sum()



# 2. With Parameter, With Return Value
def prime_sum(n):
    total = 0

    for num in range(2, n + 1):
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count == 2:
            total += num

    return total

n = int(input("Enter n: "))
result = prime_sum(n)
print("Sum =", result)


# 3. Without Parameter, With Return Value
def prime_sum():
    n = int(input("Enter n: "))
    total = 0

    for num in range(2, n + 1):
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count == 2:
            total += num

    return total

result = prime_sum()
print("Sum =", result)



# 4. With Parameter, Without Return Value
def prime_sum(n):
    total = 0

    for num in range(2, n + 1):
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count == 2:
            total += num

    print("Sum =", total)

n = int(input("Enter n: "))
prime_sum(n)