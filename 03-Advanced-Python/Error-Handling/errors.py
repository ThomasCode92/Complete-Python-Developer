# Errors

# Python raises exceptions if the interpreter encounters an error.
# Built-in Exceptions: https://docs.python.org/3/library/exceptions.html

print(1 + True)
print(1 + 'hello')


def find_in_list(idx):
    li = [1, 2, 3]
    return li[idx]


print(find_in_list(5))
