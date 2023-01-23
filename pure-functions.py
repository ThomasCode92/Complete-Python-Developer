# Pure Functions

# For a fuctions to be pure, it must follow 2 rules:
#   - Given the same input, a pure function will always return the same output.
#   - A pure function does not produce a 'side-effect'.

def multiply_by2(list):
    new_list = []
    for item in list:
        result = item * 2
        new_list.append(result)
    return new_list


list = multiply_by2([1, 2, 3])
print(list)


wizard = {
    'name': 'Merlin',
    'power': 50
}


def attack(character):
    return character['power']


print(attack(wizard))
