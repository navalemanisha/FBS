# 1. Write a program to calculate the percentage of student based on marks of any 5
# subjects.

Marathi = int (input ('Marathi subject marks 1:'))
Hindi = int (input ('Hindi subject marks 2:'))
English = int (input ('English subject marks 3:'))
Math = int (input ('Math subject marks 4:'))
Science = int (input ('Science subject marks 5:'))

total = Marathi + Hindi + English + Math + Science

percentage = ( total / 500 ) * 100
print('percentage of student marks is :',percentage)