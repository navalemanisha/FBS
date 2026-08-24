# 5. WAP to calculate selling price of book based on cost price and discount.

cost_price = int(input('Enter cost price of the book:' ))
discount = int(input('Enter discount (%)'))

discount_amount = (cost_price * discount) / 100

selling_price = cost_price - discount_amount 
print('selling price of the book =', selling_price)
