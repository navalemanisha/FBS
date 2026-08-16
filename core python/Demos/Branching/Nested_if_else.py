gender = input('Enter gender(M/F):')
age = int(input('Enter age:'))

if(gender >='F'):
    if(age >= 18):
        print('Girl is eligibal for marriage.')
    else:
        print('pahle padhai kar le.')
else:
    if(age >= 21):
        print('Boy is eligibal for marriage.')
    else:
        print('pahle kama lo.')