# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

a = int (input('enter the first angle:'))
b = int (input('enter the second angle:'))
c = int (input('enter the third angle:'))

if a>0 and b>0 and c>0 and a + b + c == 180:
    print('valid.')

else:
    print('invalid.')