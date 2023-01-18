# Global keyword
counter = 0


def count():
    global counter
    counter += 1
    return counter


print(count())
print(count())
