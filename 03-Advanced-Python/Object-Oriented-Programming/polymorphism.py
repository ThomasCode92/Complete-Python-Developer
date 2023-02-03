# Polymorphism - Fourth Pillar of OOP
# Polymorphism means that classes can share methods with the same name.
# These methods can do different things, based on what object calls them.

class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('attack...')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, number_arrows):
        self.name = name
        self.number_arrows = number_arrows

    def attack(self):
        print(f'attacking with {self.number_arrows} arrows left')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

# Both objects have a different attack method
wizard1.attack()
archer1.attack()


def player_attack(char):
    char.attack()


# Based on the passed in object, the player_attack function gives a different output
player_attack(wizard1)
player_attack(archer1)

characters = [wizard1, archer1]
for char in characters:
    char.attack()
