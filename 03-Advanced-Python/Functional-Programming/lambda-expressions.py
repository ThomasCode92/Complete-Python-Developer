# Lambda Expressions

# A Lambda expressions (in python) is a small, one-time anonymous functions
# that you don't need to run more than once.
# Syntax: lambda param: action(param)

my_list = [1, 2, 3]

doubled_list = map(lambda item: item * 2, my_list)
print(list(doubled_list))

odd_list = filter(lambda item: item % 2 != 0, my_list)
print(list(odd_list))

from functools import reduce
total = reduce(lambda acc, item: acc + item, my_list, 0)
print(total)

print(my_list)
