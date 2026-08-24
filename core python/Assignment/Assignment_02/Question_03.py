# 3. Convert distant given in feet and inches into meter and centimeter.

feet = int(input('Enter distance in feet:'))
inches = int(input('Enter distance in inches:'))

total_inches = (feet * 12) + inches
meter = total_inches * 0.0254
centimeter = total_inches * 2.54

print('meter=',meter)
print('centimeter=',centimeter)
