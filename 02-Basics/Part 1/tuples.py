# tuples
my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)
print(my_tuple[1])
print(5 in my_tuple)

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print(user.items())

new_tuple = my_tuple[1:2]
print(new_tuple)

x, y, z, *other = my_tuple
print(x, y, z, other)

print(my_tuple.count(4))
print(my_tuple.index(4))
print(len(my_tuple))
