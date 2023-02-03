# Abstraction - Second Pillar of OOP
# Abstraction means hiding away information, only give access to what is necessary.

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self._name} and I am {self._age} years old.')


player1 = PlayerCharacter('Thomas', 30)
player1.speak()  # We don't need to know how the speak method works

player1._name = '!!!' # Name is a private variable, shouldn't be overwritten
player1.speak = 'BOOOO'

print(player1.speak)
