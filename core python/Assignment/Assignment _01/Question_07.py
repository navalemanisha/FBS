# 7. Program to Find the Roots of a Quadratic Equation

a = int (input('Enter the value a:'))
b = int (input('Enter the value b:'))
c = int (input('Enter the value c:'))

d = ( b * b )-( 4 * a * c )

root1 = (- b + 0.5 ** (d)) / (2 * a )
root2 = (- b + 0.5 ** (d)) / ( 2 * a )

print('Quadratic root1 is ',root1)
print('Quadratic root2 is ',root2)
