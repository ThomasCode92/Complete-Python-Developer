# Multiple Inheritance

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

    def check_arrows(self):
        print(f'{self.number_arrows} remaining')

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hb1 = HybridBorg('borgie', 50, 100)

hb1.sign_in()
hb1.run()
hb1.attack()
hb1.check_arrows()
