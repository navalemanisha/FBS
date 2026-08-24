# 5. Write a program to enter P, T, R and calculate Compound Interest.p = int(input('Enter amount of p:'))
p = int(input('Enter principle value:'))
r = int(input('Enter rate of interest(%):'))
t = int(input('Enter time of (years):'))

amount = p*(1+r/100)**t
CI = amount - p

print('compound interest=', CI)