####1. numeric
#1.int var #variable decleration
var=10 #variable initialition
print(type(var))


#2.float
var=3.45
print(type(var))


# 3.complex
var=10+5j  #real & imaginary
print(type(var))  


####2. text
# 1.set
var='hello'
var="hello"
var='''hello'''
"""this is second line.
this is next line"""
print(type(var))

#### 3.sequencial

# 1.list
var=[10,20,30,40]
print(type(var))

# 2.tuple
var=(10,20,30,40)
print(type(var))

# 3.range
var=range(1,11)
print(type(var))

####4.set type
# 1.set
var={10,20,30,}
print(type(var))

# 2.frozenset
var=frozenset({10,20,30,})
print(type(var))

#### 5.mapping
# 1.dict
var={'id':'101','name':'xyz'}
print(type(var))

#### 6.others
# 1.boolean
var=True
print(type(var))

# 2.none
var=None
print(type(var))

