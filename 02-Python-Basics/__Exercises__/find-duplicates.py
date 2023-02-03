# Exercise: Check for duplicates in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# Solution ('Don't use sets')
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

if len(duplicates) > 0:
    print(f'The list contains duplicates: {duplicates}!')
else:
    print('No duplicates found!')
