for i in range(1, 6):
     for j in range(1, 6):
         if(j == i+1 or j == i+3 or i == j+3 or i == j+1):
             print('$', end= ' ')
         else:
             print('*', end= ' ')
     print()