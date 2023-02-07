with open('test.txt', mode='r+') as my_file:
    print(my_file.read())
    my_file.seek(0)

    text = my_file.write('Hey, it\'s me!')
    print(text)

with open('test.txt', mode='w') as my_file:
    text = my_file.write(':)')
    print(text)

with open('test.txt', mode='a') as my_file:
    text = my_file.write(':)')
    print(text)

try:
    with open('app/sad.txt', mode='r') as my_file:
        text = my_file.read()
        print(text)
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err
