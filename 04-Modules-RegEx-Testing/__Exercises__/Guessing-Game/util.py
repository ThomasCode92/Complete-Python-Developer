from sys import argv


def get_args():
    return argv[1:] if len(argv) == 3 else [1, 10]

def get_min_max(num1, num2):
    return [int(num1), int(num2)]
