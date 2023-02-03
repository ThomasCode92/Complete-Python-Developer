# Inheritance - Third Pillar of OOP
# Inheritance allows new objects to take on the properties of existing objects.

class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, number_arrows):
        self.name = name
        self.number_arrows = number_arrows

    def attack(self):
        print(f'attacking with {self.number_arrows} arrows left')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

wizard1.sign_in()
wizard1.attack()
archer1.attack()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))
