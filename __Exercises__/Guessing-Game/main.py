from random import randint
from util import get_args, get_min_max

minArg, maxArg = get_args()
min, max = get_min_max(minArg, maxArg)

answer = randint(min, max)

while True:
    try:
        print('Cheating: ', answer)
        guess = input(f'Guess a number {min}~{max}: ')
        number = int(guess)

        if number > min and number < max + 1:
            if number == answer:
                print('You are a genius!')
                break
        else:
            print(f'Please enter a number between {min}~{max}! ')

    except ValueError:
        print('Please enter a number!')
        continue
