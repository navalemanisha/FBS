correct_userid = 'admin'
correct_password = '1234'

for i in range(3):
    userid = input('Enter User ID: ')
    password = input('Enter Password: ')

    if userid == correct_userid and password == correct_password:
        print('Login Successful!')
        break
    else:
        print("Incorrect User ID or Password.")

        if i < 2:
            print("Please try again.")
        else:
            print("3 attempts completed. Program terminated.")