# Scope

# What variables do I have access to?
# 1 - start with local scope
# 2 - parent local scope
# 3 - global scope
# 4 - built in python functions

if True:
    x = 10

def some_func():
    total = 100

print(x)
# print(total) => total is not defined because of the function scope

a = 1

def confusion():
    a = 5
    return a

print(a)
print(confusion())
