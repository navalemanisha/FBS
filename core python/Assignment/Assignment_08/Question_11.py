# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

# 1. Without Parameter, Without Return Value
def armstrong():
    n = int(input("Enter number: "))
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10

    if total == original:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

armstrong()



# 2. With Parameter, With Return Value
def armstrong(n):
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10

    return total == original

n = int(input("Enter number: "))
result = armstrong(n)

if result:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


    # 3. Without Parameter, With Return Value
def armstrong():
    n = int(input("Enter number: "))
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10

    return total == original

result = armstrong()

if result:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# 4. With Parameter, Without Return Value
def armstrong(n):
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10

    if total == original:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

n = int(input("Enter number: "))
armstrong(n)