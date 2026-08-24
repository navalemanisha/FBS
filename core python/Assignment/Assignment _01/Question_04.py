# 4. Write a program to enter P, T, R and calculate simple Interest.p = float (input('Enter principal amount:'))

r = float (input('Enter rate of interest(%):'))
t = float (input('Enter time of (years):'))

si = (p*r*t)/100

print('simple interest =',si)