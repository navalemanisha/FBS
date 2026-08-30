# 1. Write a program to calculate area of rectangle

# 1. Without passing Parameter, Without Return Value
def area():
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))

    area =  length * breadth

    print("Area of Rectangle =", {area})
area()

# 2. With Parameter, With Return Value
def area(length, breadth):
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))

    area = length * breadth

    print('Area of Rectangle =', area)

x = 10
y = 20
area (x,y)

# 3. Without passing Parameter, With Return Value
def area():
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))

    area = length * breadth
    return area

res = area()
print(res)




# # 1. Without Parameter, Without Return Value
# def rectangle():
#     l = float(input("Enter length: "))
#     b = float(input("Enter breadth: "))
#     area = l * b
#     print("Area =", area)

# rectangle()


# # 2. Without Parameter, With Return Value
# def rectangle():
#     l = float(input("Enter length: "))
#     b = float(input("Enter breadth: "))
#     return l * b

# area = rectangle()
# print("Area =", area)


# # 3. With Parameter, Without Return Value
# def rectangle(l, b):
#     area = l * b
#     print("Area =", area)

# l = float(input("Enter length: "))
# b = float(input("Enter breadth: "))
# rectangle(l, b)


# # 4. With Parameter, With Return Value

# def rectangle(l, b):
#     return l * b

# l = float(input("Enter length: "))
# b = float(input("Enter breadth: "))
# area = rectangle(l, b)
# print("Area =", area)