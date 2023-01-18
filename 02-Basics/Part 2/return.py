# Return
def sum(num1, num2):
    return num1 + num2


print(sum(4, 5))

total = sum(10, 5)
print(sum(10, total))


def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
        print('hi')
    return another_func(num1, num2)


total = sum(10, 20)
print(total)
