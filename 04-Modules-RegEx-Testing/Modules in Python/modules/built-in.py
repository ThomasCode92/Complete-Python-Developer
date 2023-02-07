import random
import sys as system

print(random)
help(random)
print(dir(random))


print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

firstname = system.argv[1]
lastname = system.argv[2]

print(f'Hello {firstname} {lastname}!')
