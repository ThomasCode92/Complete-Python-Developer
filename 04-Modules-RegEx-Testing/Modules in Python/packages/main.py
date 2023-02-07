from utility import multiply, divide
from shopping.more_shopping import shopping_cart

print(shopping_cart)
print(shopping_cart.buy('apple'))

print(divide(5, 2))
print(multiply(5, 2))

print(__name__)

if __name__ == '__main__':
    print('Do something...')


class Student():
    pass


student1 = Student()
print(type(student1))  # => <class '__main__.Student'>
