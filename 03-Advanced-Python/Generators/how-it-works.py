# Under the Hood of Generators

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3])


class MyRange():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyRange.current < self.last:
            num = MyRange.current
            MyRange.current += 1
            return num
        raise StopIteration


gen = MyRange(0, 10)
for i in gen:
    print(i)
