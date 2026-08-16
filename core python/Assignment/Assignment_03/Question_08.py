import random
userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "admin" and password == "1234":
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)

    num = int(input("Enter captcha: "))

    if num == captcha:
        print("Success")
    else:
        print("Failed")
else:
    print("Invalid User ID or Password")