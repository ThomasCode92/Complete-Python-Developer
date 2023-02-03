# Useful functions - map, filter, zip & reduce

# Map
def multiply_by2(item):
    return item * 2

my_list = [1, 2, 3]
result = map(multiply_by2, my_list)

print(list(result))
print(my_list)

# Filter
def only_odd(item):
    return item % 2 != 0

my_list = [1, 2, 3]
result = filter(only_odd, my_list)

print(list(result))
print(my_list)

# Zip
my_list1 = [1, 2, 3]
my_list2 = [10, 20, 30]

result = zip(my_list1, my_list2)
print(list(result))
print(my_list1)
print(my_list2)

# Reduce
from functools import reduce

my_list = [1, 2, 3]

def accumulator(acc, item):
    return item + acc

result = reduce(accumulator, my_list, 0)
print(result)
print(my_list)
