for i in range(1,10):
    pass

# 2. break: to stop the loop
# for i in range (1,10):
#     if(i == 3):
#         continue
#     print(i)

# 3.continue: to stop current iteraction
for i in range(1,10):
    if(i ==5):
        continue
    print(i)

#4. else: will execute when loop executed successfully
for i in range(1,10):
    if(i ==3):
        continue
    print(i)
else:
    print('else executed')

5.
for i in range(1,10):
    if(i ==3):
        break
    print(i)
else:
    print('else executed')
    
