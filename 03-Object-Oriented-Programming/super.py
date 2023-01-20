# The super() method

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, email, power):
        super().__init__(email)  # super() refers to the parent class (in this case, User)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


wizard1 = Wizard('Merlin', 'merlin@gmail.com', 50)
print(wizard1.email)

# Introspection - The ability to determine the type of an object at runtime
print(dir(wizard1))
