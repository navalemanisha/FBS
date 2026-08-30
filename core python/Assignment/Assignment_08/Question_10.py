# 10. Write a program to check if entered year is a leap year or not.

# 1. Without Parameter, Without Return Value
def leap_year():
    year = int(input("Enter year: "))

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

leap_year()

# 2. With Parameter, With Return Value
def leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

year = int(input("Enter year: "))
result = leap_year(year)

if result:
    print("Leap Year")
else:
    print("Not a Leap Year")

    # 3. Without Parameter, With Return Value
def leap_year():
    year = int(input("Enter year: "))

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

result = leap_year()

if result:
    print("Leap Year")
else:
    print("Not a Leap Year")


# 4. With Parameter, Without Return Value
def leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

year = int(input("Enter year: "))
leap_year(year)