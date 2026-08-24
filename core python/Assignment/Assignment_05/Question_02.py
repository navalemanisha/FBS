# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(n):
    print("Student", i + 1)

    m1 = float(input("Enter marks of Subject 1: "))
    m2 = float(input("Enter marks of Subject 2: "))
    m3 = float(input("Enter marks of Subject 3: "))
    m4 = float(input("Enter marks of Subject 4: "))
    m5 = float(input("Enter marks of Subject 5: "))

    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    print("Percentage =", percentage, "%")

    total_percentage = total_percentage + percentage

average = total_percentage / n

print("Average Percentage =", average, "%")