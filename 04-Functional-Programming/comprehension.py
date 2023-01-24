# Comprehensions

# Comprehensions are a quick way to create a list, set or dictionary.

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# List Comprehension offers a shorter syntax for creating a new list
# based on the values of an existing list.
my_list = [char for char in 'hello']
my_numbers = [num ** 2 for num in range(0, 100)]
even_numbers = [num ** 2 for num in range(0, 100) if num % 2 == 0]

print(my_list)
print(my_numbers)
print(even_numbers)

# Set and Dictionary Comprehension
my_set = {char for char in 'hello'}
print(my_set)

simple_dict = {'a': 1, 'b': 2}
my_dict = {key.upper(): value ** 2 for key, value in simple_dict.items()}
print(my_dict)

my_dict = {num: num * 2 for num in [1, 2, 3]}
print(my_dict)
