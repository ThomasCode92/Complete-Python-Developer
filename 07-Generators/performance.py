# Generators and Performance

# Generators are really useful when calculating large sets of data, particularly when
# long loops are used and there is no need to story store that memory.

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1}ms')
        return result
    return wrapper


num = 1000000


@performance
def long_time():
    print('Func 1')
    for i in range(num):
        i*5


@performance
def long_time2():
    print('Func 2')
    for i in list(range(num)):
        i*5


long_time()
long_time2()
