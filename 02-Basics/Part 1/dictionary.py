# dictionary
dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}

my_list = [
    {'a': [1, 2, 3], 'b': 'hello', 'x': True},
    {'a': [4, 5, 6], 'b': 'hello', 'x': True}
]

print(my_list[0]['a'][2])
print(dictionary['a'][1])

# dictionary methods
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

user2 = dict(name='John Doe')

print(user.get('age', 55))
print(user2.get('name'))

print('basket' in user)
print('hello' in user.keys())
print('hello' in user.values())

print(user.items())

user.clear()
print(user)

user = user2.copy()
print(user)

print(user.pop('name'))
print(user)

user.update({'name': 'John Doe'})
user.update({'age': 20})
user.update({'age': 55})
print(user)
