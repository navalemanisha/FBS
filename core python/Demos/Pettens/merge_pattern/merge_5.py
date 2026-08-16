for i  in range(1,6):
    k=1
    for j in range(1,6-i):
        print(' ',end=' ')
    
    for j in range(1,i+1):
         print(j,end=' ')
         k+=1
         
    for j in range(1,i,):
            print(j,end=' ')
            k+=1

    print()  
    
# for i  in range(1,6):
#     for j in range(1,6-i):
#         print(' ',end=' ')
    
#     for j in range(1,i*2):
#          print(j,end=' ') 
#     print()