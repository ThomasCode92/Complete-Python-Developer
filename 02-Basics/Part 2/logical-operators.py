# Logical Operators
print(4 < 5)
print('a' > 'A')
print(1 < 2 > 3 < 4)
print(1 >= 0)
print(1 <= 0)
print(0 != 0)

print(not (True))
print(not 1 == 1)

print("-----")

# is vs ==
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

print(True is 1)
print('1' is '1')
print([] is [])
print(10 is 10)
print([1, 2, 3] is [1, 2, 3])

a = [1, 2, 3]
b = a
print(a is b)
