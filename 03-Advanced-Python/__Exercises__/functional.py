from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()

result = map(capitalize, my_pets)
print(list(result))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

sorted_numbers = sorted(my_numbers)

result = zip(my_strings, sorted_numbers)
print(list(result))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def over_50(item):
    return item > 50

result = filter(over_50, scores)
print(list(result))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def sum(acc, item):
    return acc + item

result = reduce(sum, (my_numbers + scores), 0)
print(result)
