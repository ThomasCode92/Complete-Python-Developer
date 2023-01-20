# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Felix', 4)
cat2 = Cat('Oscar', 1)
cat3 = Cat('Smudge', 9)


# 2 Create a function that finds the oldest cat
def get_oldest_cat(*args):
    ages = []
    for item in args:
        ages.append(item.age)
    return max(ages)


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {get_oldest_cat(cat1, cat2, cat3)} years old.')
