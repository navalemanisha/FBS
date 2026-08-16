p = int(input('Enter amount of p:'))
r = int(input('Enter rate of interest(%):'))
t = int(input('Enter time of (years):'))

amount = p*(1+r/100)**t
CI = amount - p

print('compound interest=', CI)