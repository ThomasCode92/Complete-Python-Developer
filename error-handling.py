# Error Handling

# Allow the Python script to continue running, even if there are errors

while True:
    try:
        age = int(input('What is your age? '))
        print(age)

        print(f'Ten divided by your age is {10 / age}')
    except ValueError:
        print('Please enter a number!')
    except ZeroDivisionError:
        print('Please enter an age higher than 0!')
    else:
        print('Thank you!')
        break
    finally:
        print('Ok, I\'m finally done!')


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'Please enter numbers, {err}!')


result = sum(1, '2')
print(result)


def divide(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'Please enter numbers greater than 0, {err}!')


result = divide(2, 0)
print(result)
