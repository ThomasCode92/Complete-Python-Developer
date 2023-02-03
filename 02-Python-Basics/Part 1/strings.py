# Fundamental Data Types
# string
print(type("hi hello there 24!"))
username = 'supercoder'
password = 'supersecret'
long_string = '''
    W0W
    0 0
    ---
'''

print(long_string)

# string concatenation
first_name = 'Thomas'
last_name = 'Code92'
full_name = first_name + ' ' + last_name

print(full_name)

# escape sequences
weather = "It's \"kind of\" sunny\n\t hope you have a good day!"
print(weather)

# formatted strings
name = 'Johnny'
age = 55

print('Hi {}. You are {} years old'.format(name, age))
print('Hi {1}. You are {0} years old'.format(name, age))
print('Hi {new_name}. You are {age} years old'.format(
    age=100, new_name="Sally"))
print(f'Hi {name}. You are {age} years old')

# string indexes
numbers = '01234567'

print(numbers[1])
print(numbers[0:2])  # [start:stop]
print(numbers[0:8:2])  # [start:stop:stepover]
print(numbers[-2])
print(numbers[::-1])
