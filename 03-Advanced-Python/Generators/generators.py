# Generators

# A Generator creates a sequence of values over time.
# The range function is a built-in Generator in Python

result = list(range(10))
print(result)


def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result


my_list = make_list(100)
print(my_list)

# Create and use a Generator
def generator_func(num):
    for i in range(num):
        yield i * 2


for item in generator_func(10):
    print(item)

g = generator_func(100)
print(g)
print(next(g))
print(next(g))
print(next(g))
