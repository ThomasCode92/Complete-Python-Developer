# Functions
def say_hello():
    print('hellooo!!')

say_hello()

# Parameters and Arguments
def say_hello(name):
    print(f'hellooo {name}!!')

say_hello('Thomas')

# Default Parameters and Keyword Arguments
def say_hello(name, greeting='hello'):
    print(f'{greeting} {name}!')

say_hello(greeting='hi', name='Thomas')
say_hello('Thomas')
