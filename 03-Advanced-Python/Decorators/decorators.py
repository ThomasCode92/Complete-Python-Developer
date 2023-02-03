# Decorators

# A decorator is a design pattern that allows a user to add new
# functionality to an existing function without modifying its structure.

def my_decorator(func):
    def wrap_func():
        print('*******')
        func()
        print('*******')
    return wrap_func


@my_decorator
def hello():
    print('hellloo')


hello()
my_decorator(hello)()

# Decorator Pattern

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func


@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


hello('Greetings...')
hello('Hello', ':(')
