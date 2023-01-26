# Functions in Python

# Functions are First Class Citizens in Python, this means that they can be
# treated as a values, pass them as arguments and to return a function from another function.

def hello():
    print('hellooo')

greet = hello
greet()

def hello(func):
    func()

def greet():
    print('hellooo')

hello(greet)

# Higher Order Function
# A function is called Higher Order Function if it contains other
# functions as a parameter or returns a function as an output.

def greet(func):
    func()

def greet():
    def func():
        return 5
    return func
