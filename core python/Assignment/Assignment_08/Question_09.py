# 9. Write a program to check if entered number is a palindrome or
# not.

# 1. Without Parameter, Without Return Value
def palindrome():
    n = int(input("Enter number: "))
    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    if original == rev:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")

palindrome()


# 2. With Parameter, With Return Value
def palindrome(n):
    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    return original == rev

n = int(input("Enter number: "))
result = palindrome(n)

if result:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

    # 3. Without Parameter, With Return Value
def palindrome():
    n = int(input("Enter number: "))
    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    return original == rev

result = palindrome()

if result:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


# 4. With Parameter, Without Return Value
def palindrome(n):
    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    if original == rev:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")

n = int(input("Enter number: "))
palindrome(n)
