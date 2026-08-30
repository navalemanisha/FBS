# 6. Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms

# 1. Without passing Parameter, Without Return Value
def fibonacci():
    n = int(input("Enter number of terms: "))
    a = 1
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci()


# 2. With passing Parameter, With Return Value
def fibonacci(n):
    a = 1
    b = 1
    series = []

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series

n = int(input("Enter number of terms: "))
result = fibonacci(n)
print(*result)


# 3. Without passing Parameter, With Return Value
def fibonacci():
    n = int(input("Enter number of terms: "))
    a = 1
    b = 1
    series = []

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series

result = fibonacci()
print(*result)


# 4. With passing Parameter, Without Return Value
def fibonacci(n):
    a = 1
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)
