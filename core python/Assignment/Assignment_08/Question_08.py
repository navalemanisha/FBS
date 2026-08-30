# 8. Write a program find reverse of a number

# 1. Without Parameter, Without Return Value

def reverse():
    n = int(input("Enter number: "))
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    print("Reverse =", rev)

reverse()

# 2. With Parameter, With Return Value
def reverse(n):
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    return rev

n = int(input("Enter number: "))
result = reverse(n)
print("Reverse =", result)


# 3. Without Parameter, With Return Value
def reverse():
    n = int(input("Enter number: "))
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    return rev

result = reverse()
print("Reverse =", result)


# 4. With Parameter, Without Return Value
def reverse(n):
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    print("Reverse =", rev)

n = int(input("Enter number: "))
reverse(n)