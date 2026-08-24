#  Write a program print following patterns: 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

n = 5

# Increasing
for i in range(1, n + 1):
    print("* " * i)

# Decreasing
for i in range(n - 1, 0, -1):
    print("* " * i)