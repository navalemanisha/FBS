# 2. Write a program to calculate area of circle

# 1. Without Parameter, Without Return Value
def circle():
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print("Area =", area)

circle()


# 2. With Parameter, With Return Value
def circle(r):
    return 3.14 * r * r

r = float(input("Enter radius: "))
area = circle(r)
print("Area =", area)

# 3. Without Parameter, With Return Value
def circle():
    r = float(input("Enter radius: "))
    return 3.14 * r * r

area = circle()
print("Area =", area)


# 4. With Parameter, Without Return Value
def circle(r):
    area = 3.14 * r * r
    print("Area =", area)

r = float(input("Enter radius: "))
circle(r)
