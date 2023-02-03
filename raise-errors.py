# Raise Errors

# Scripts can raise exceptions (or throw errors) to signal that something went wrong.

while True:
    try:
        number = int(input('What is your favorite number? '))
        # ...
        raise ValueError('Not a good number!')
    except ValueError as err:
        print(f'Something went wrong, {err}!')
        break
