# Dunder (or Magic) Methods
# Dunder methods allow instances of a class to interact with the built-in functions and operators.
# The word “dunder” comes from “double underscore”.

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'for_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return 'yess??'

    def __getitem__(self, idx):
        return self.my_dict[idx]

    def __del__(self):
        print('deleted')


action_figure = Toy('red', 0)

print(action_figure.__str__())
print(str(action_figure))
print(str('my string'))

print(len(action_figure))
print(action_figure())

print(action_figure['name'])

del action_figure
