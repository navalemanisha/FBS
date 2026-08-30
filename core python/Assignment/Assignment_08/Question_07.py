# 7. Write a program to find sum of digits of a number.

# 1. Without Parameter, Without Return Value
def sum_digits():
    n = int(input("Enter number: "))
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    print("Sum of digits =", total)

sum_digits()


# 2. With Parameter, With Return Value
def sum_digits(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total

n = int(input("Enter number: "))
result = sum_digits(n)
print("Sum of digits =", result)


# 3. Without Parameter, With Return Value
def sum_digits():
    n = int(input("Enter number: "))
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total

result = sum_digits()
print("Sum of digits =", result)


# 4. With Parameter, Without Return Value
def sum_digits(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    print("Sum of digits =", total)

n = int(input("Enter number: "))
sum_digits(n)