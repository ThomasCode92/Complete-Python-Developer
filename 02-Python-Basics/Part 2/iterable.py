# Iterables
# iterable -> list, dictionary, tuple, set, string
# iterate -> one by one check each item in the collection

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False,
}

for item in user:
    print(item, user[item])

for item in user.items():
    key, value = item
    print(item, key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for key, value in user.items():
    print(key, value)
