# 12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3 digit number: "))

if num < 100 or num > 999:
    print("Please enter a 3 digit number")
else:
    if (num // 100) == (num % 10):
        print("Palindrome number")
    else:
        print("Not a palindrome number")