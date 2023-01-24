my_list = [5, 4, 3]

# Square
squared_list = map(lambda item: pow(item, 2), my_list)
print(list(squared_list))

# List Sorting
tuple_list = [(0, 2), (10, -1), (4, 3), (9, 9)]
tuple_list.sort(key=lambda item: item[1])
print(tuple_list)
