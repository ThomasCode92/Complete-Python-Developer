def highest_even(list):
    result = 0
    for item in list:
        if item % 2 == 0 and item > result:
            result = item
    return result

def highest_even(list):
    evens = []
    for item in list:
        if item % 2 == 0:
           evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))
