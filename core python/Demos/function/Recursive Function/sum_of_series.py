def SOS(n):
    if(n<=0):
        return 0
    else:
        return n + SOS(n-1)

num = int(input('Enter number:'))
res = SOS(num)
print(res)