# 6. Write a program to calculate profit or loss.

cost_price = int(input('enter the cost_price:'))
selling_price = int(input('enter the selling_price:'))

if selling_price < cost_price:
    print('enter profit.')
elif selling_price > cost_price:
    print('enter loss.')
else:
    print('no profit' ,'no loss')